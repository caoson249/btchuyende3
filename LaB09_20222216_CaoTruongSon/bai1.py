import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/diem_sinhvien.csv")

# 1. Kiểm tra giá trị thiếu
print("Số giá trị thiếu mỗi cột:")
print(df.isna().sum())

# 2. Điền thiếu cho DiemQT, DiemThi bằng trung bình
df["DiemQT"] = df["DiemQT"].fillna(df["DiemQT"].mean())
df["DiemThi"] = df["DiemThi"].fillna(df["DiemThi"].mean())

# 3. Điền thiếu HoTen
df["HoTen"] = df["HoTen"].fillna("ChuaCapNhat")

# 4. Tính lại DiemTK
df["DiemTK"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# 5. Xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "D"

df["XepLoai"] = df["DiemTK"].apply(xep_loai)

# Xuất kết quả
print("\nDữ liệu sau xử lý:")
print(df.head())

# Lưu file mới (nếu cần)
df.to_csv("diem_sinhvien_clean.csv", index=False)