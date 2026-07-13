# Xổ số Miền Nam (XSMN) Analysis

Sử dụng GitHub Action để tự động hoá thu thập và phân tích kết quả xổ số miền Nam hàng ngày.

Dự án này dựa trên [khiemdoan/vietnam-lottery-xsmb-analysis](https://github.com/khiemdoan/vietnam-lottery-xsmb-analysis), chuyển đổi từ XSMB sang XSMN.


## An Giang (09-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **622936** |
| Giải nhất | 15860 |
| Giải nhì | 28251 |
| Giải ba | 38344, 93766 |
| Giải tư | 47742, 54035, 25932, 83121, 03597, 29534, 04726 |
| Giải năm | 03388 |
| Giải sáu | 5921, 8134, 7068 |
| Giải bảy | 907 |
| Giải tám | 06 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [angiang.csv](data/angiang.csv) | [angiang.json](data/angiang.json) | [angiang.parquet](data/angiang.parquet) |
| 2-digits | [angiang-2-digits.csv](data/angiang-2-digits.csv) | [angiang-2-digits.json](data/angiang-2-digits.json) | [angiang-2-digits.parquet](data/angiang-2-digits.parquet) |
| Sparse   | [angiang-sparse.csv](data/angiang-sparse.csv) | [angiang-sparse.json](data/angiang-sparse.json) | [angiang-sparse.parquet](data/angiang-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 4.

  Mean: 9.36. Standard deviation: 2.88.

  ![Heatmap](images/angiang/heatmap.jpg)

  ![Top 10](images/angiang/top-10.jpg)

  ![Distribution](images/angiang/distribution.jpg)

</details>

---

## Bình Dương (10-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **663795** |
| Giải nhất | 26361 |
| Giải nhì | 05911 |
| Giải ba | 14613, 73129 |
| Giải tư | 21603, 02774, 76628, 00405, 02429, 75680, 03202 |
| Giải năm | 06650 |
| Giải sáu | 0442, 0711, 6702 |
| Giải bảy | 638 |
| Giải tám | 63 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [binhduong.csv](data/binhduong.csv) | [binhduong.json](data/binhduong.json) | [binhduong.parquet](data/binhduong.parquet) |
| 2-digits | [binhduong-2-digits.csv](data/binhduong-2-digits.csv) | [binhduong-2-digits.json](data/binhduong-2-digits.json) | [binhduong-2-digits.parquet](data/binhduong-2-digits.parquet) |
| Sparse   | [binhduong-sparse.csv](data/binhduong-sparse.csv) | [binhduong-sparse.json](data/binhduong-sparse.json) | [binhduong-sparse.parquet](data/binhduong-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 2.

  Mean: 9.36. Standard deviation: 2.95.

  ![Heatmap](images/binhduong/heatmap.jpg)

  ![Top 10](images/binhduong/top-10.jpg)

  ![Distribution](images/binhduong/distribution.jpg)

</details>

---

## Bình Phước (11-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **087990** |
| Giải nhất | 95576 |
| Giải nhì | 72550 |
| Giải ba | 48388, 92355 |
| Giải tư | 65233, 32508, 59867, 90453, 79152, 90939, 90937 |
| Giải năm | 00877 |
| Giải sáu | 7390, 5458, 4974 |
| Giải bảy | 715 |
| Giải tám | 96 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [binhphuoc.csv](data/binhphuoc.csv) | [binhphuoc.json](data/binhphuoc.json) | [binhphuoc.parquet](data/binhphuoc.parquet) |
| 2-digits | [binhphuoc-2-digits.csv](data/binhphuoc-2-digits.csv) | [binhphuoc-2-digits.json](data/binhphuoc-2-digits.json) | [binhphuoc-2-digits.parquet](data/binhphuoc-2-digits.parquet) |
| Sparse   | [binhphuoc-sparse.csv](data/binhphuoc-sparse.csv) | [binhphuoc-sparse.json](data/binhphuoc-sparse.json) | [binhphuoc-sparse.parquet](data/binhphuoc-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 19. Min: 3.

  Mean: 9.54. Standard deviation: 3.39.

  ![Heatmap](images/binhphuoc/heatmap.jpg)

  ![Top 10](images/binhphuoc/top-10.jpg)

  ![Distribution](images/binhphuoc/distribution.jpg)

</details>

---

## Bình Thuận (09-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **763530** |
| Giải nhất | 32946 |
| Giải nhì | 23369 |
| Giải ba | 47742, 34981 |
| Giải tư | 79965, 57609, 91542, 52404, 96779, 74905, 62259 |
| Giải năm | 05324 |
| Giải sáu | 1786, 6328, 5235 |
| Giải bảy | 362 |
| Giải tám | 36 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [binhthuan.csv](data/binhthuan.csv) | [binhthuan.json](data/binhthuan.json) | [binhthuan.parquet](data/binhthuan.parquet) |
| 2-digits | [binhthuan-2-digits.csv](data/binhthuan-2-digits.csv) | [binhthuan-2-digits.json](data/binhthuan-2-digits.json) | [binhthuan-2-digits.parquet](data/binhthuan-2-digits.parquet) |
| Sparse   | [binhthuan-sparse.csv](data/binhthuan-sparse.csv) | [binhthuan-sparse.json](data/binhthuan-sparse.json) | [binhthuan-sparse.parquet](data/binhthuan-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 16. Min: 3.

  Mean: 9.36. Standard deviation: 2.87.

  ![Heatmap](images/binhthuan/heatmap.jpg)

  ![Top 10](images/binhthuan/top-10.jpg)

  ![Distribution](images/binhthuan/distribution.jpg)

</details>

---

## Bạc Liêu (07-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **709492** |
| Giải nhất | 93146 |
| Giải nhì | 42513 |
| Giải ba | 80482, 76768 |
| Giải tư | 83703, 71807, 16405, 33975, 64086, 18977, 35001 |
| Giải năm | 07253 |
| Giải sáu | 4780, 4696, 6440 |
| Giải bảy | 776 |
| Giải tám | 15 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [baclieu.csv](data/baclieu.csv) | [baclieu.json](data/baclieu.json) | [baclieu.parquet](data/baclieu.parquet) |
| 2-digits | [baclieu-2-digits.csv](data/baclieu-2-digits.csv) | [baclieu-2-digits.json](data/baclieu-2-digits.json) | [baclieu-2-digits.parquet](data/baclieu-2-digits.parquet) |
| Sparse   | [baclieu-sparse.csv](data/baclieu-sparse.csv) | [baclieu-sparse.json](data/baclieu-sparse.json) | [baclieu-sparse.parquet](data/baclieu-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 21. Min: 0.

  Mean: 9.36. Standard deviation: 3.55.

  ![Heatmap](images/baclieu/heatmap.jpg)

  ![Top 10](images/baclieu/top-10.jpg)

  ![Distribution](images/baclieu/distribution.jpg)

</details>

---

## Bến Tre (07-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **877777** |
| Giải nhất | 59078 |
| Giải nhì | 00083 |
| Giải ba | 74773, 87723 |
| Giải tư | 31096, 91065, 09745, 19481, 41878, 39406, 99838 |
| Giải năm | 07271 |
| Giải sáu | 1669, 4092, 7478 |
| Giải bảy | 639 |
| Giải tám | 05 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [bentre.csv](data/bentre.csv) | [bentre.json](data/bentre.json) | [bentre.parquet](data/bentre.parquet) |
| 2-digits | [bentre-2-digits.csv](data/bentre-2-digits.csv) | [bentre-2-digits.json](data/bentre-2-digits.json) | [bentre-2-digits.parquet](data/bentre-2-digits.parquet) |
| Sparse   | [bentre-sparse.csv](data/bentre-sparse.csv) | [bentre-sparse.json](data/bentre-sparse.json) | [bentre-sparse.parquet](data/bentre-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 0.

  Mean: 9.36. Standard deviation: 3.54.

  ![Heatmap](images/bentre/heatmap.jpg)

  ![Top 10](images/bentre/top-10.jpg)

  ![Distribution](images/bentre/distribution.jpg)

</details>

---

## Cà Mau (06-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **738323** |
| Giải nhất | 10652 |
| Giải nhì | 49279 |
| Giải ba | 99982, 58550 |
| Giải tư | 48183, 50157, 50142, 79923, 83730, 56983, 75590 |
| Giải năm | 01204 |
| Giải sáu | 2607, 7332, 0081 |
| Giải bảy | 081 |
| Giải tám | 46 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [camau.csv](data/camau.csv) | [camau.json](data/camau.json) | [camau.parquet](data/camau.parquet) |
| 2-digits | [camau-2-digits.csv](data/camau-2-digits.csv) | [camau-2-digits.json](data/camau-2-digits.json) | [camau-2-digits.parquet](data/camau-2-digits.parquet) |
| Sparse   | [camau-sparse.csv](data/camau-sparse.csv) | [camau-sparse.json](data/camau-sparse.json) | [camau-sparse.parquet](data/camau-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 3.

  Mean: 9.36. Standard deviation: 2.88.

  ![Heatmap](images/camau/heatmap.jpg)

  ![Top 10](images/camau/top-10.jpg)

  ![Distribution](images/camau/distribution.jpg)

</details>

---

## Cần Thơ (08-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **214463** |
| Giải nhất | 37814 |
| Giải nhì | 38961 |
| Giải ba | 81701, 89733 |
| Giải tư | 15745, 90096, 17661, 80852, 53410, 72295, 94913 |
| Giải năm | 02659 |
| Giải sáu | 4415, 2927, 9735 |
| Giải bảy | 179 |
| Giải tám | 68 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [cantho.csv](data/cantho.csv) | [cantho.json](data/cantho.json) | [cantho.parquet](data/cantho.parquet) |
| 2-digits | [cantho-2-digits.csv](data/cantho-2-digits.csv) | [cantho-2-digits.json](data/cantho-2-digits.json) | [cantho-2-digits.parquet](data/cantho-2-digits.parquet) |
| Sparse   | [cantho-sparse.csv](data/cantho-sparse.csv) | [cantho-sparse.json](data/cantho-sparse.json) | [cantho-sparse.parquet](data/cantho-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 2.

  Mean: 9.36. Standard deviation: 2.94.

  ![Heatmap](images/cantho/heatmap.jpg)

  ![Top 10](images/cantho/top-10.jpg)

  ![Distribution](images/cantho/distribution.jpg)

</details>

---

## Hậu Giang (11-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **883669** |
| Giải nhất | 31090 |
| Giải nhì | 31751 |
| Giải ba | 81554, 12774 |
| Giải tư | 89656, 91993, 15853, 84749, 44227, 79836, 46711 |
| Giải năm | 01022 |
| Giải sáu | 6295, 1631, 4903 |
| Giải bảy | 821 |
| Giải tám | 45 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [hau giang.csv](data/hau giang.csv) | [hau giang.json](data/hau giang.json) | [hau giang.parquet](data/hau giang.parquet) |
| 2-digits | [hau giang-2-digits.csv](data/hau giang-2-digits.csv) | [hau giang-2-digits.json](data/hau giang-2-digits.json) | [hau giang-2-digits.parquet](data/hau giang-2-digits.parquet) |
| Sparse   | [hau giang-sparse.csv](data/hau giang-sparse.csv) | [hau giang-sparse.json](data/hau giang-sparse.json) | [hau giang-sparse.parquet](data/hau giang-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 23. Min: 3.

  Mean: 9.54. Standard deviation: 3.74.

  ![Heatmap](images/hau giang/heatmap.jpg)

  ![Top 10](images/hau giang/top-10.jpg)

  ![Distribution](images/hau giang/distribution.jpg)

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

## Long An (11-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **016397** |
| Giải nhất | 76759 |
| Giải nhì | 91688 |
| Giải ba | 49183, 16713 |
| Giải tư | 72738, 30463, 88865, 28434, 84625, 59731, 07730 |
| Giải năm | 09678 |
| Giải sáu | 1974, 4792, 5347 |
| Giải bảy | 565 |
| Giải tám | 28 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [longan.csv](data/longan.csv) | [longan.json](data/longan.json) | [longan.parquet](data/longan.parquet) |
| 2-digits | [longan-2-digits.csv](data/longan-2-digits.csv) | [longan-2-digits.json](data/longan-2-digits.json) | [longan-2-digits.parquet](data/longan-2-digits.parquet) |
| Sparse   | [longan-sparse.csv](data/longan-sparse.csv) | [longan-sparse.json](data/longan-sparse.json) | [longan-sparse.parquet](data/longan-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 4.

  Mean: 9.54. Standard deviation: 2.91.

  ![Heatmap](images/longan/heatmap.jpg)

  ![Top 10](images/longan/top-10.jpg)

  ![Distribution](images/longan/distribution.jpg)

</details>

---

## Sóc Trăng (08-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **708297** |
| Giải nhất | 93546 |
| Giải nhì | 22596 |
| Giải ba | 75292, 42218 |
| Giải tư | 34254, 65279, 58378, 53818, 37095, 64652, 65183 |
| Giải năm | 03903 |
| Giải sáu | 6193, 8563, 1264 |
| Giải bảy | 916 |
| Giải tám | 48 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [soctrang.csv](data/soctrang.csv) | [soctrang.json](data/soctrang.json) | [soctrang.parquet](data/soctrang.parquet) |
| 2-digits | [soctrang-2-digits.csv](data/soctrang-2-digits.csv) | [soctrang-2-digits.json](data/soctrang-2-digits.json) | [soctrang-2-digits.parquet](data/soctrang-2-digits.parquet) |
| Sparse   | [soctrang-sparse.csv](data/soctrang-sparse.csv) | [soctrang-sparse.json](data/soctrang-sparse.json) | [soctrang-sparse.parquet](data/soctrang-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 18. Min: 1.

  Mean: 9.36. Standard deviation: 2.95.

  ![Heatmap](images/soctrang/heatmap.jpg)

  ![Top 10](images/soctrang/top-10.jpg)

  ![Distribution](images/soctrang/distribution.jpg)

</details>

---

## TP. HCM (04-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **185542** |
| Giải nhất | 10124 |
| Giải nhì | 31285 |
| Giải ba | 38864, 73603 |
| Giải tư | 10817, 03857, 08323, 03793, 77113, 00517, 86435 |
| Giải năm | 07853 |
| Giải sáu | 7252, 8102, 2155 |
| Giải bảy | 817 |
| Giải tám | 98 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [hcm.csv](data/hcm.csv) | [hcm.json](data/hcm.json) | [hcm.parquet](data/hcm.parquet) |
| 2-digits | [hcm-2-digits.csv](data/hcm-2-digits.csv) | [hcm-2-digits.json](data/hcm-2-digits.json) | [hcm-2-digits.parquet](data/hcm-2-digits.parquet) |
| Sparse   | [hcm-sparse.csv](data/hcm-sparse.csv) | [hcm-sparse.json](data/hcm-sparse.json) | [hcm-sparse.parquet](data/hcm-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 33. Min: 8.

  Mean: 18.9. Standard deviation: 4.63.

  ![Heatmap](images/hcm/heatmap.jpg)

  ![Top 10](images/hcm/top-10.jpg)

  ![Distribution](images/hcm/distribution.jpg)

</details>

---

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

## Trà Vinh (10-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **325002** |
| Giải nhất | 44392 |
| Giải nhì | 78976 |
| Giải ba | 27148, 60269 |
| Giải tư | 59086, 07496, 83400, 23409, 59974, 72448, 78305 |
| Giải năm | 06982 |
| Giải sáu | 8085, 7124, 5351 |
| Giải bảy | 900 |
| Giải tám | 51 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [travinh.csv](data/travinh.csv) | [travinh.json](data/travinh.json) | [travinh.parquet](data/travinh.parquet) |
| 2-digits | [travinh-2-digits.csv](data/travinh-2-digits.csv) | [travinh-2-digits.json](data/travinh-2-digits.json) | [travinh-2-digits.parquet](data/travinh-2-digits.parquet) |
| Sparse   | [travinh-sparse.csv](data/travinh-sparse.csv) | [travinh-sparse.json](data/travinh-sparse.json) | [travinh-sparse.parquet](data/travinh-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 4.

  Mean: 9.36. Standard deviation: 3.11.

  ![Heatmap](images/travinh/heatmap.jpg)

  ![Top 10](images/travinh/top-10.jpg)

  ![Distribution](images/travinh/distribution.jpg)

</details>

---

## Tây Ninh (09-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **306050** |
| Giải nhất | 50830 |
| Giải nhì | 91654 |
| Giải ba | 93553, 11469 |
| Giải tư | 95262, 57634, 26427, 83873, 17826, 08351, 08686 |
| Giải năm | 06573 |
| Giải sáu | 8610, 0724, 7486 |
| Giải bảy | 754 |
| Giải tám | 27 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [tayninh.csv](data/tayninh.csv) | [tayninh.json](data/tayninh.json) | [tayninh.parquet](data/tayninh.parquet) |
| 2-digits | [tayninh-2-digits.csv](data/tayninh-2-digits.csv) | [tayninh-2-digits.json](data/tayninh-2-digits.json) | [tayninh-2-digits.parquet](data/tayninh-2-digits.parquet) |
| Sparse   | [tayninh-sparse.csv](data/tayninh-sparse.csv) | [tayninh-sparse.json](data/tayninh-sparse.json) | [tayninh-sparse.parquet](data/tayninh-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 2.

  Mean: 9.36. Standard deviation: 3.06.

  ![Heatmap](images/tayninh/heatmap.jpg)

  ![Top 10](images/tayninh/top-10.jpg)

  ![Distribution](images/tayninh/distribution.jpg)

</details>

---

## Vĩnh Long (10-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **073565** |
| Giải nhất | 91553 |
| Giải nhì | 08409 |
| Giải ba | 05155, 43291 |
| Giải tư | 28647, 07105, 08241, 32095, 97330, 54446, 92219 |
| Giải năm | 08141 |
| Giải sáu | 1990, 3659, 5057 |
| Giải bảy | 095 |
| Giải tám | 95 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [vinhlong.csv](data/vinhlong.csv) | [vinhlong.json](data/vinhlong.json) | [vinhlong.parquet](data/vinhlong.parquet) |
| 2-digits | [vinhlong-2-digits.csv](data/vinhlong-2-digits.csv) | [vinhlong-2-digits.json](data/vinhlong-2-digits.json) | [vinhlong-2-digits.parquet](data/vinhlong-2-digits.parquet) |
| Sparse   | [vinhlong-sparse.csv](data/vinhlong-sparse.csv) | [vinhlong-sparse.json](data/vinhlong-sparse.json) | [vinhlong-sparse.parquet](data/vinhlong-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 18. Min: 3.

  Mean: 9.36. Standard deviation: 3.22.

  ![Heatmap](images/vinhlong/heatmap.jpg)

  ![Top 10](images/vinhlong/top-10.jpg)

  ![Distribution](images/vinhlong/distribution.jpg)

</details>

---

## Vũng Tàu (07-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **168986** |
| Giải nhất | 36041 |
| Giải nhì | 91832 |
| Giải ba | 61154, 98970 |
| Giải tư | 26316, 60123, 48489, 87993, 24265, 85456, 76916 |
| Giải năm | 01128 |
| Giải sáu | 5118, 1091, 1722 |
| Giải bảy | 077 |
| Giải tám | 18 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [vungtau.csv](data/vungtau.csv) | [vungtau.json](data/vungtau.json) | [vungtau.parquet](data/vungtau.parquet) |
| 2-digits | [vungtau-2-digits.csv](data/vungtau-2-digits.csv) | [vungtau-2-digits.json](data/vungtau-2-digits.json) | [vungtau-2-digits.parquet](data/vungtau-2-digits.parquet) |
| Sparse   | [vungtau-sparse.csv](data/vungtau-sparse.csv) | [vungtau-sparse.json](data/vungtau-sparse.json) | [vungtau-sparse.parquet](data/vungtau-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 15. Min: 4.

  Mean: 9.36. Standard deviation: 2.74.

  ![Heatmap](images/vungtau/heatmap.jpg)

  ![Top 10](images/vungtau/top-10.jpg)

  ![Distribution](images/vungtau/distribution.jpg)

</details>

---

## Đà Lạt (28-06-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **635343** |
| Giải nhất | 49624 |
| Giải nhì | 88765 |
| Giải ba | 30446, 52689 |
| Giải tư | 58770, 14459, 90452, 29223, 05074, 60465, 00945 |
| Giải năm | 09976 |
| Giải sáu | 7944, 0026, 1675 |
| Giải bảy | 017 |
| Giải tám | 16 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [dalat.csv](data/dalat.csv) | [dalat.json](data/dalat.json) | [dalat.parquet](data/dalat.parquet) |
| 2-digits | [dalat-2-digits.csv](data/dalat-2-digits.csv) | [dalat-2-digits.json](data/dalat-2-digits.json) | [dalat-2-digits.parquet](data/dalat-2-digits.parquet) |
| Sparse   | [dalat-sparse.csv](data/dalat-sparse.csv) | [dalat-sparse.json](data/dalat-sparse.json) | [dalat-sparse.parquet](data/dalat-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 17. Min: 4.

  Mean: 9.54. Standard deviation: 2.95.

  ![Heatmap](images/dalat/heatmap.jpg)

  ![Top 10](images/dalat/top-10.jpg)

  ![Distribution](images/dalat/distribution.jpg)

</details>

---

## Đồng Nai (08-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **061248** |
| Giải nhất | 40651 |
| Giải nhì | 53913 |
| Giải ba | 92425, 62190 |
| Giải tư | 48289, 10993, 90963, 35884, 10410, 97093, 32999 |
| Giải năm | 03402 |
| Giải sáu | 5837, 9611, 4288 |
| Giải bảy | 811 |
| Giải tám | 48 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [dongnai.csv](data/dongnai.csv) | [dongnai.json](data/dongnai.json) | [dongnai.parquet](data/dongnai.parquet) |
| 2-digits | [dongnai-2-digits.csv](data/dongnai-2-digits.csv) | [dongnai-2-digits.json](data/dongnai-2-digits.json) | [dongnai-2-digits.parquet](data/dongnai-2-digits.parquet) |
| Sparse   | [dongnai-sparse.csv](data/dongnai-sparse.csv) | [dongnai-sparse.json](data/dongnai-sparse.json) | [dongnai-sparse.parquet](data/dongnai-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 19. Min: 2.

  Mean: 9.36. Standard deviation: 3.16.

  ![Heatmap](images/dongnai/heatmap.jpg)

  ![Top 10](images/dongnai/top-10.jpg)

  ![Distribution](images/dongnai/distribution.jpg)

</details>

---

## Đồng Tháp (06-07-2026)

| Giải | Kết quả |
| :--- | :------ |
| Đặc biệt | **497852** |
| Giải nhất | 01422 |
| Giải nhì | 22357 |
| Giải ba | 27799, 45705 |
| Giải tư | 29880, 05713, 76396, 64836, 08839, 72144, 47838 |
| Giải năm | 01562 |
| Giải sáu | 4859, 4196, 7958 |
| Giải bảy | 642 |
| Giải tám | 27 |

### Dữ liệu

|          | CSV | JSON | Parquet |
|----------|-----|------|---------|
| Raw      | [dongthap.csv](data/dongthap.csv) | [dongthap.json](data/dongthap.json) | [dongthap.parquet](data/dongthap.parquet) |
| 2-digits | [dongthap-2-digits.csv](data/dongthap-2-digits.csv) | [dongthap-2-digits.json](data/dongthap-2-digits.json) | [dongthap-2-digits.parquet](data/dongthap-2-digits.parquet) |
| Sparse   | [dongthap-sparse.csv](data/dongthap-sparse.csv) | [dongthap-sparse.json](data/dongthap-sparse.json) | [dongthap-sparse.parquet](data/dongthap-sparse.parquet) |

<details>
  <summary>Phân tích</summary>

  Max: 19. Min: 2.

  Mean: 9.36. Standard deviation: 3.01.

  ![Heatmap](images/dongthap/heatmap.jpg)

  ![Top 10](images/dongthap/top-10.jpg)

  ![Distribution](images/dongthap/distribution.jpg)

</details>

---
