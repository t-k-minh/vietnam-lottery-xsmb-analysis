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

    weekday = today.weekday()
    stations = get_stations_for_date(weekday)

    if not stations:
        print(f'Không có đài nào quay ngày {today}')
        exit(0)

    print(f'=== XSMN {today} ===')
    print(f'Đài quay: {", ".join(stations)}\n')

    station_results = []

    for station_name in stations:
        station_code = STATION_CODES.get(station_name, station_name.lower().replace(" ", ""))
        print(f'--- {station_name} ({station_code}) ---')

        lottery = Lottery(station_name)
        lottery.load()

        # Fetch dữ liệu mới
        begin_date = lottery.get_last_date()
        delta = (today - begin_date).days
        if delta > 0:
            for i in range(1, delta + 1):
                fetch_date = begin_date + timedelta(days=i)
                if fetch_date.weekday() == weekday or delta > 7:
                    print(f'  Fetching: {fetch_date}')
                    lottery.fetch(fetch_date)
            lottery.generate_dataframes()
            lottery.dump()

        # Phân tích + tạo biểu đồ
        if not lottery.get_raw_data().empty:
            result = generate_station_plots(lottery, f'images/{station_code}')
            if result:
                station_results.append(result)
                print(f'  OK — {len(lottery.get_raw_data())} ngày dữ liệu\n')
        else:
            print(f'  Không có dữ liệu\n')

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
        print(f'=== Hoàn thành: {len(station_results)} đài, README.md đã cập nhật ===')
    else:
        print('=== Không có dữ liệu để hiển thị ===')
