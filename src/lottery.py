__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from copy import copy
from datetime import date

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper

from dtos import XSMNResult, XSMNResultList
from stations import get_station_code


class Lottery:
    def __init__(self, station_name: str) -> None:
        self._http = CloudScraper()
        self._station_name = station_name
        self._station_code = get_station_code(station_name)
        self._data: dict[date, XSMNResult] = {}
        self._raw_data: pd.DataFrame = pd.DataFrame()
        self._2_digits_data: pd.DataFrame = pd.DataFrame()
        self._sparse_data: pd.DataFrame = pd.DataFrame()
        self._begin_date = date.today()
        self._last_date = date.today()

    def load(self) -> None:
        file_path = f'data/{self._station_code}.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = XSMNResultList.model_validate_json(f.read())
            for d in data.root:
                self._data[d.date] = d
        except FileNotFoundError:
            pass  # Lần đầu chạy, chưa có dữ liệu
        self.generate_dataframes()

    def dump(self) -> None:
        def _dump(df: pd.DataFrame, file_name: str) -> None:
            df.to_csv(f'data/{file_name}.csv', index=False)
            df.to_json(f'data/{file_name}.json', orient='records', date_format='iso', indent=2, index=False)
            df.to_parquet(f'data/{file_name}.parquet', index=False)

        _dump(self._raw_data, self._station_code)
        _dump(self._2_digits_data, f'{self._station_code}-2-digits')
        _dump(self._sparse_data, f'{self._station_code}-sparse')

    def fetch(self, selected_date: date) -> bool:
        """Fetch kết quả XSMN từ minhngoc.net.vn cho đài và ngày đã cho.
        Trả về True nếu fetch thành công."""
        url = f'https://www.minhngoc.net.vn/ket-qua-xo-so/mien-nam/{selected_date:%d-%m-%Y}.html'
        resp = self._http.get(url)
        if resp.status_code != 200:
            return False

        soup = BeautifulSoup(resp.text, 'lxml')

        # Tìm tất cả các bảng kết quả (class="rightcl")
        tables = soup.find_all('table', class_='rightcl')

        for table in tables:
            tinh_td = table.find('td', class_='tinh')
            if not tinh_td:
                continue
            tinh_name = tinh_td.get_text(strip=True)

            # So sánh tên đài (không phân biệt hoa thường, bỏ khoảng trắng)
            if tinh_name.lower().strip() != self._station_name.lower().strip():
                continue

            # Tìm mã đài
            matinh_td = table.find('td', class_='matinh')
            station_code = matinh_td.get_text(strip=True) if matinh_td else ""

            # Parse các giải
            def get_prize_text(class_name: str) -> list[str]:
                td = table.find('td', class_=class_name)
                if not td:
                    return []
                return [div.get_text(strip=True) for div in td.find_all('div')]

            special = get_prize_text('giaidb')
            prize1 = get_prize_text('giai1')
            prize2 = get_prize_text('giai2')
            prize3 = get_prize_text('giai3')
            prize4 = get_prize_text('giai4')
            prize5 = get_prize_text('giai5')
            prize6 = get_prize_text('giai6')
            prize7 = get_prize_text('giai7')
            prize8 = get_prize_text('giai8')

            # Kiểm tra đủ dữ liệu
            if not (special and prize1 and prize2 and prize3 and
                    len(prize4) >= 7 and prize5 and len(prize6) >= 3 and prize7 and prize8):
                continue

            result = XSMNResult(
                date=selected_date,
                station=self._station_name,
                station_code=station_code,
                special=int(special[0]),
                prize1=int(prize1[0]),
                prize2=int(prize2[0]),
                prize3_1=int(prize3[0]), prize3_2=int(prize3[1]),
                prize4_1=int(prize4[0]), prize4_2=int(prize4[1]),
                prize4_3=int(prize4[2]), prize4_4=int(prize4[3]),
                prize4_5=int(prize4[4]), prize4_6=int(prize4[5]),
                prize4_7=int(prize4[6]),
                prize5=int(prize5[0]),
                prize6_1=int(prize6[0]), prize6_2=int(prize6[1]), prize6_3=int(prize6[2]),
                prize7=int(prize7[0]),
                prize8=int(prize8[0]),
            )
            self._data[result.date] = result
            return True

        return False

    def generate_dataframes(self) -> None:
        if not self._data:
            self._raw_data = pd.DataFrame()
            self._2_digits_data = pd.DataFrame()
            self._sparse_data = pd.DataFrame()
            return

        self._raw_data = pd.DataFrame([d.model_dump() for d in self._data.values()])
        self._raw_data['date'] = pd.to_datetime(self._raw_data['date'])
        # Bỏ cột station, station_code khi phân tích số
        numeric_cols = [c for c in self._raw_data.columns if c not in ('date', 'station', 'station_code')]
        self._raw_data[numeric_cols] = self._raw_data[numeric_cols].astype('int64')

        self._2_digits_data = self._raw_data[['date'] + numeric_cols].copy()
        self._2_digits_data[numeric_cols] = self._2_digits_data[numeric_cols].apply(lambda x: x % 100)

        self._sparse_data = pd.concat(
            [
                self._2_digits_data[['date']],
                pd.DataFrame(np.zeros((self._2_digits_data.shape[0], 100), dtype=int)),
            ],
            axis=1,
        )
        self._sparse_data.iloc[:, 1:] = self._sparse_data.iloc[:, 1:].astype('int64')
        for i in range(self._2_digits_data.shape[0]):
            counts = self._2_digits_data.iloc[i, 1:].value_counts()
            for k, v in counts.items():
                self._sparse_data.iloc[i, k + 1] = int(v)

        begin_date = self._raw_data['date'].min()
        self._begin_date = begin_date.to_pydatetime().date()
        last_date = self._raw_data['date'].max()
        self._last_date = last_date.to_pydatetime().date()

    def get_raw_data(self) -> pd.DataFrame:
        return self._raw_data

    def get_2_digits_data(self) -> pd.DataFrame:
        return self._2_digits_data

    def get_sparse_data(self) -> pd.DataFrame:
        return self._sparse_data

    def get_last_date(self) -> date:
        return self._last_date

    def get_station_name(self) -> str:
        return self._station_name

    def get_station_code(self) -> str:
        return self._station_code
