__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from lottery import Lottery
from analyze import generate_station_plots
from stations import get_stations_for_date, STATION_CODES
from templates import Render

if __name__ == '__main__':
    tz = ZoneInfo('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)
    today = now.date()
    if now.time() < time(16, 30):
        today -= timedelta(days=1)

    # Thu thập tất cả đài trong 7 ngày qua
    all_stations = set()
    for i in range(7):
        check_date = today - timedelta(days=i)
        weekday = check_date.weekday()
        stations = get_stations_for_date(weekday)
        all_stations.update(stations)

    print(f'=== Fetch ALL {len(all_stations)} stations ===')
    print(f'Backfill 1 nam tu {today - timedelta(days=365)} den {today}\n')

    station_results = []

    for station_name in sorted(all_stations):
        station_code = STATION_CODES.get(station_name, station_name.lower().replace(" ", ""))
        print(f'--- {station_name} ({station_code}) ---')

        lottery = Lottery(station_name)
        lottery.load()

        # Fetch 1 nam
        from_date = today - timedelta(days=365)
        delta = (today - from_date).days + 1

        for i in range(delta):
            fetch_date = from_date + timedelta(days=i)
            # Chi fetch ngay dung thu cua dai
            weekday_of_fetch = fetch_date.weekday()
            stations_of_day = get_stations_for_date(weekday_of_fetch)
            if station_name in stations_of_day:
                # Kiem tra chua co du lieu
                if fetch_date not in lottery._data:
                    print(f'  Fetching: {fetch_date}')
                    lottery.fetch(fetch_date)

        lottery.generate_dataframes()
        lottery.dump()

        if not lottery.get_raw_data().empty:
            result = generate_station_plots(lottery, f'images/{station_code}')
            if result:
                station_results.append(result)
                print(f'  OK — {len(lottery.get_raw_data())} ngay\n')
        else:
            print(f'  Khong co du lieu\n')

    # Render README
    if station_results:
        render = Render()
        context = {
            'station_results': station_results,
            'date': today.strftime('%d-%m-%Y'),
        }
        content = render('README.j2', context)
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'=== Hoan thanh: {len(station_results)} dai, README.md da cap nhat ===')
    else:
        print('=== Khong co du lieu de hien thi ===')
