# Xổ số Miền Nam (XSMN) Analysis

Sử dụng GitHub Action để tự động hoá thu thập và phân tích kết quả xổ số miền Nam hàng ngày.

Dự án này dựa trên [khiemdoan/vietnam-lottery-xsmb-analysis](https://github.com/khiemdoan/vietnam-lottery-xsmb-analysis), chuyển đổi từ XSMB sang XSMN.


## Tiền Giang (12-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **898582** |
| Giải nhất | 11865 |
| Giải nhì | 22368 |
| Giải ba | 62096, 77715 |
| Giải tư | 91401, 31112, 32870, 82026, 82316, 80048, 37225 |
| Giải năm | 06522 |
| Giải sáu | 3841, 4469, 9759 |
| Giải bảy | 252 |
| Giải tám | 07 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [tiengiang.csv](data/tiengiang.csv) | [tiengiang.json](data/tiengiang.json) | [tiengiang.parquet](data/tiengiang.parquet) |
| 2-digits | [tiengiang-2-digits.csv](data/tiengiang-2-digits.csv) | [tiengiang-2-digits.json](data/tiengiang-2-digits.json) | [tiengiang-2-digits.parquet](data/tiengiang-2-digits.parquet) |
| Sparse   | [tiengiang-sparse.csv](data/tiengiang-sparse.csv) | [tiengiang-sparse.json](data/tiengiang-sparse.json) | [tiengiang-sparse.parquet](data/tiengiang-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 126. Min: 14.

  Mean: 65.7. Standard deviation: 19.92.

  ![Heatmap](images/tiengiang/heatmap.jpg)

  ![Top 10](images/tiengiang/top-10.jpg)

  ![Distribution](images/tiengiang/distribution.jpg)

</details>

---

## Kiên Giang (12-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **913490** |
| Giải nhất | 05117 |
| Giải nhì | 43178 |
| Giải ba | 28938, 00448 |
| Giải tư | 08116, 22527, 47561, 86576, 22291, 23493, 46016 |
| Giải năm | 07846 |
| Giải sáu | 8335, 7796, 0344 |
| Giải bảy | 455 |
| Giải tám | 99 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [kiengiang.csv](data/kiengiang.csv) | [kiengiang.json](data/kiengiang.json) | [kiengiang.parquet](data/kiengiang.parquet) |
| 2-digits | [kiengiang-2-digits.csv](data/kiengiang-2-digits.csv) | [kiengiang-2-digits.json](data/kiengiang-2-digits.json) | [kiengiang-2-digits.parquet](data/kiengiang-2-digits.parquet) |
| Sparse   | [kiengiang-sparse.csv](data/kiengiang-sparse.csv) | [kiengiang-sparse.json](data/kiengiang-sparse.json) | [kiengiang-sparse.parquet](data/kiengiang-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 127. Min: 14.

  Mean: 65.7. Standard deviation: 22.45.

  ![Heatmap](images/kiengiang/heatmap.jpg)

  ![Top 10](images/kiengiang/top-10.jpg)

  ![Distribution](images/kiengiang/distribution.jpg)

</details>

---

## Đà Lạt (12-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **579838** |
| Giải nhất | 48236 |
| Giải nhì | 61616 |
| Giải ba | 70723, 06136 |
| Giải tư | 03080, 83183, 25421, 53881, 20906, 63817, 19432 |
| Giải năm | 07721 |
| Giải sáu | 4134, 8317, 1305 |
| Giải bảy | 579 |
| Giải tám | 65 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [dalat.csv](data/dalat.csv) | [dalat.json](data/dalat.json) | [dalat.parquet](data/dalat.parquet) |
| 2-digits | [dalat-2-digits.csv](data/dalat-2-digits.csv) | [dalat-2-digits.json](data/dalat-2-digits.json) | [dalat-2-digits.parquet](data/dalat-2-digits.parquet) |
| Sparse   | [dalat-sparse.csv](data/dalat-sparse.csv) | [dalat-sparse.json](data/dalat-sparse.json) | [dalat-sparse.parquet](data/dalat-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 3. Min: 0.

  Mean: 0.36. Standard deviation: 0.64.

  ![Heatmap](images/dalat/heatmap.jpg)

  ![Top 10](images/dalat/top-10.jpg)

  ![Distribution](images/dalat/distribution.jpg)

</details>

---
