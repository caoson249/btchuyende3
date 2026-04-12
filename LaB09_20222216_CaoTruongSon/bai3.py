import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/nhansu.csv")

# 1. Chuẩn hóa GioiTinh
df["GioiTinh"] = df["GioiTinh"].str.strip().str.lower()
df["GioiTinh"] = df["GioiTinh"].replace({
    "nam": "Nam",
    "nữ": "Nữ",
    "nu": "Nữ",
    "female": "Nữ",
    "male": "Nam"
})

# 2. Chuẩn hóa PhongBan (viết hoa chữ cái đầu)
df["PhongBan"] = df["PhongBan"].str.strip().str.title()

# 3. Xóa khoảng trắng thừa trong HoTen
df["HoTen"] = df["HoTen"].str.strip()

# 4. Đổi tên cột
df = df.rename(columns={
    "MaNV": "ma_nv",
    "HoTen": "ho_ten",
    "GioiTinh": "gioi_tinh",
    "PhongBan": "phong_ban",
    "Luong": "luong"
})

# Kết quả
print(df.head())

# Lưu file mới (nếu cần)
df.to_csv("nhansu_clean.csv", index=False)