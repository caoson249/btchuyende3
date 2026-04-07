import pandas as pd
import numpy as np

# ===== 1. Tạo dữ liệu mẫu =====
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08"],
    "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D",
              "Hoang Van E", "Do Thi F", "Vu Van G", "Bui Thi H"],
    "Toan": [8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 6.0, 8.8],
    "Ly": [7.5, 6.5, 8.5, 7.0, 8.2, 7.8, 6.2, 9.0],
    "Hoa": [8.0, 7.2, 9.1, 6.8, 8.5, 7.0, 6.5, 8.7]
}

df_create = pd.DataFrame(data)

# ===== 2. Lưu thành file CSV =====
df_create.to_csv("diem_sinhvien.csv", index=False)

# ===== 3. Đọc lại file CSV =====
df = pd.read_csv("diem_sinhvien.csv")

# ===== 4. Xem dữ liệu =====
print("=== 5 dòng đầu ===")
print(df.head())

print("\n=== 5 dòng cuối ===")
print(df.tail())

print("\n=== Thông tin dữ liệu ===")
print(df.info())

print("\n=== Thống kê mô tả ===")
print(df.describe())