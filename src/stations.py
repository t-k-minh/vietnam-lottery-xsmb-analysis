__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

# Lịch quay XSMN theo thứ (0=Thứ 2, 6=Chủ nhật)
# Nguồn: https://www.minhngoc.net.vn/thong-tin/lich-quay-so-mo-thuong.html

SCHEDULE: dict[int, list[str]] = {
    0: ["TP. HCM", "Đồng Tháp", "Cà Mau"],       # Thứ 2
    1: ["Bến Tre", "Vũng Tàu", "Bạc Liêu"],                # Thứ 3
    2: ["Đồng Nai", "Cần Thơ", "Sóc Trăng"],               # Thứ 4
    3: ["Tây Ninh", "An Giang", "Bình Thuận"],              # Thứ 5
    4: ["Vĩnh Long", "Bình Dương", "Trà Vinh"],             # Thứ 6
    5: ["TP. HCM", "Long An", "Bình Phước", "Hậu Giang"],  # Thứ 7
    6: ["Tiền Giang", "Kiên Giang", "Đà Lạt"],             # Chủ nhật
}

# Mapping ten dai → ma dai (dung cho ten file)
STATION_CODES: dict[str, str] = {
    "TP. HCM": "hcm",
    "Đồng Tháp": "dongthap",
    "Cà Mau": "camau",
    "Bến Tre": "bentre",
    "Vũng Tàu": "vungtau",
    "Bạc Liêu": "baclieu",
    "Đồng Nai": "dongnai",
    "Cần Thơ": "cantho",
    "Sóc Trăng": "soctrang",
    "Tây Ninh": "tayninh",
    "An Giang": "angiang",
    "Bình Thuận": "binhthuan",
    "Vĩnh Long": "vinhlong",
    "Bình Dương": "binhduong",
    "Trà Vinh": "travinh",
    "Long An": "longan",
    "Bình Phước": "binhphuoc",
    "Hậu Giang": "hau giang",
    "Tiền Giang": "tiengiang",
    "Kiên Giang": "kiengiang",
    "Đà Lạt": "dalat",
}

def get_stations_for_date(weekday: int) -> list[str]:
    """Trả về danh sách đài quay theo thứ trong tuần."""
    return SCHEDULE.get(weekday, [])

def get_station_code(station_name: str) -> str:
    """Trả về mã đài từ tên đài."""
    return STATION_CODES.get(station_name, station_name.lower().replace(" ", ""))
