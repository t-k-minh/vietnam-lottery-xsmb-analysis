# Xổ số Miền Nam (XSMN) Analysis

Sử dụng GitHub Action để tự động hoá thu thập và phân tích kết quả xổ số miền Nam hàng ngày.

Dự án này dựa trên [khiemdoan/vietnam-lottery-xsmb-analysis](https://github.com/khiemdoan/vietnam-lottery-xsmb-analysis), chuyển đổi từ XSMB sang XSMN.

## Lịch quay

| Thứ | Các đài |
|------|---------|
| Thứ 2 | TP. Hồ Chí Minh, Đồng Tháp, Cà Mau |
| Thứ 3 | Bến Tre, Vũng Tàu, Bạc Liêu |
| Thứ 4 | Đồng Nai, Cần Thơ, Sóc Trăng |
| Thứ 5 | Tây Ninh, An Giang, Bình Thuận |
| Thứ 6 | Vĩnh Long, Bình Dương, Trà Vinh |
| Thứ 7 | TP. Hồ Chí Minh, Long An, Bình Phước, Hậu Giang |
| Chủ nhật | Tiền Giang, Kiên Giang, Đà Lạt |

## Dữ liệu

Dữ liệu được tự động cập nhật hàng ngày. Mỗi đài có file riêng:

| Đài | CSV | JSON | Parquet |
|-----|-----|------|---------|
| TP. HCM | [hcm.csv](data/hcm.csv) | [hcm.json](data/hcm.json) | [hcm.parquet](data/hcm.parquet) |
| Đồng Tháp | [dongthap.csv](data/dongthap.csv) | [dongthap.json](data/dongthap.json) | [dongthap.parquet](data/dongthap.parquet) |
| Cà Mau | [camau.csv](data/camau.csv) | [camau.json](data/camau.json) | [camau.parquet](data/camau.parquet) |
| ... | ... | ... | ... |

## Cài đặt & Chạy

```bash
git clone https://github.com/t-k-minh/vietnam-lottery-xsmb-analysis.git
cd vietnam-lottery-xsmb-analysis
uv sync --frozen --no-dev
uv run src/run.py
```

Hoặc dùng `curl`/`wget` tải dữ liệu trực tiếp:

```bash
curl -O https://raw.githubusercontent.com/t-k-minh/vietnam-lottery-xsmb-analysis/refs/heads/main/data/hcm.csv
```

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/t-k-minh/vietnam-lottery-xsmb-analysis/refs/heads/main/data/hcm.csv')
df.info()
```

## Cấu trúc giải thưởng XSMN

| Giải | Số chữ số | Số giải |
|------|----------|---------|
| Đặc biệt | 6 | 1 |
| Nhất | 5 | 1 |
| Nhì | 5 | 1 |
| Ba | 5 | 2 |
| Tư | 5 | 7 |
| Năm | 5 | 1 |
| Sáu | 4 | 3 |
| Bảy | 3 | 1 |
| Tám | 2 | 1 |
