__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from lottery import Lottery
from stations import get_stations_for_date, STATION_CODES

if __name__ == '__main__':
    tz = ZoneInfo('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)
    today = now.date()

    # Xác định ngày cần fetch (nếu trước 16:30 thì lấy ngày hôm trước, XSMN quay ~16:15)
    if now.time() < time(16, 30):
        today -= timedelta(days=1)

    weekday = today.weekday()
    stations = get_stations_for_date(weekday)

    if not stations:
        print(f'Không có đài nào quay ngày {today}')
        exit(0)

    print(f'Fetching XSMN for {today} ({now.strftime("%A")}): {", ".join(stations)}')

    for station_name in stations:
        station_code = STATION_CODES.get(station_name, station_name.lower().replace(" ", ""))
        print(f'\n--- {station_name} ({station_code}) ---')

        lottery = Lottery(station_name)
        lottery.load()

        # Fetch từ ngày cuối có dữ liệu đến hôm nay
        begin_date = lottery.get_last_date()
        delta = (today - begin_date).days

        if delta <= 0:
            print(f'  Đã có dữ liệu mới nhất')
            continue

        for i in range(1, delta + 1):
            fetch_date = begin_date + timedelta(days=i)
            # Chỉ fetch ngày đúng thứ của đài này (hoặc fetch tất cả nếu đang backfill)
            if fetch_date.weekday() == weekday or delta > 7:
                print(f'  Fetching: {fetch_date}')
                lottery.fetch(fetch_date)

        lottery.generate_dataframes()
        lottery.dump()
        print(f'  Done. Total records: {len(lottery.get_raw_data())}')
