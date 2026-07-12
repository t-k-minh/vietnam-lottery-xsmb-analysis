__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from datetime import date

from pydantic import BaseModel, RootModel


class XSMNResult(BaseModel):
    date: date
    station: str       # tên đài, ví dụ "Tiền Giang"
    station_code: str  # mã đài, ví dụ "XSTG"

    special: int       # 6 chữ số

    prize1: int        # 5 chữ số
    prize2: int        # 5 chữ số
    prize3_1: int      # 5 chữ số
    prize3_2: int
    prize4_1: int      # 5 chữ số (7 giải)
    prize4_2: int
    prize4_3: int
    prize4_4: int
    prize4_5: int
    prize4_6: int
    prize4_7: int
    prize5: int        # 5 chữ số
    prize6_1: int      # 4 chữ số (3 giải)
    prize6_2: int
    prize6_3: int
    prize7: int        # 3 chữ số
    prize8: int        # 2 chữ số


class XSMNResultList(RootModel):
    root: list[XSMNResult]
