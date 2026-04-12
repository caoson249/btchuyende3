import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/khaosat.csv")

# 1. Chuẩn hóa CoLamThem → 1/0
df["CoLamThem"] = df["CoLamThem"].str.strip().str.lower()
df["CoLamThem"] = df["CoLamThem"].replace({
    "yes": 1, "y": 1, "có": 1,
    "no": 0, "n": 0, "không": 0
})

# 2. Chuẩn hóa MucDoHaiLong về 1–5
df["MucDoHaiLong"] = df["MucDoHaiLong"].replace({
    "Rất hài lòng": 5,
    "Hài lòng": 4,
    "Bình thường": 3,
    "Không hài lòng": 2,
    "Rất không hài lòng": 1
})
df["MucDoHaiLong"] = df["MucDoHaiLong"].astype(int)

# 3. Đổi tên cột
df = df.rename(columns={
    "MaSV": "ma_sv",
    "GioHocMoiNgay": "gio_hoc_moi_ngay",
    "MucDoHaiLong": "muc_do_hai_long",
    "CoLamThem": "co_lam_them"
})

# 4. Loại bỏ bản ghi giờ học < 0
df = df[df["gio_hoc_moi_ngay"] >= 0]

# 5. Đếm số SV làm thêm / không làm thêm
thong_ke = df["co_lam_them"].value_counts()

print("Dữ liệu sau xử lý:")
print(df)

print("\nThống kê làm thêm:")
print(thong_ke)