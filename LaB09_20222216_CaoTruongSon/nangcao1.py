import pandas as pd
import numpy as np

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/tuyensinh.csv")

# ======================
# 1. Chuẩn hóa dữ liệu
# ======================

# Họ tên
df["HoTen"] = df["HoTen"].str.strip().str.title()

# Giới tính
df["GioiTinh"] = df["GioiTinh"].str.strip().str.lower()
df["GioiTinh"] = df["GioiTinh"].replace({
    "nam": "Nam",
    "male": "Nam",
    "nữ": "Nữ",
    "nu": "Nữ",
    "female": "Nữ"
})

# Ngày sinh
df["NgaySinh"] = pd.to_datetime(df["NgaySinh"], errors="coerce")

# ======================
# 2. Xử lý dữ liệu thiếu
# ======================

# Điểm → dùng trung bình
for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    df[col] = df[col].fillna(df[col].mean())

# Ngày sinh → giữ nguyên (không nên tự suy đoán)
# HoTen, GioiTinh → có thể fill nếu cần
df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# ======================
# 3. Phát hiện điểm lỗi
# ======================

dieu_kien_loi = (
    (df["DiemToan"] < 0) | (df["DiemToan"] > 10) |
    (df["DiemVan"] < 0) | (df["DiemVan"] > 10) |
    (df["DiemAnh"] < 0) | (df["DiemAnh"] > 10)
)

diem_loi = df[dieu_kien_loi]
print("Học sinh có điểm lỗi:")
print(diem_loi)

# Có thể xử lý: thay bằng NaN rồi fill lại
for col in ["DiemToan", "DiemVan", "DiemAnh"]:
    df.loc[(df[col] < 0) | (df[col] > 10), col] = np.nan
    df[col] = df[col].fillna(df[col].mean())

# ======================
# 4. Tính tổng điểm
# ======================
df["TongDiem"] = df["DiemToan"] + df["DiemVan"] + df["DiemAnh"]

# ======================
# 5. Phân nhóm qcut
# ======================
df["XepHang"] = pd.qcut(df["TongDiem"], q=3, labels=["Thấp", "Trung bình", "Cao"])

# ======================
# 6. Thống kê theo khu vực
# ======================
thong_ke = df.groupby("KhuVuc").agg(
    SoLuong=("MaHS", "count"),
    DiemTB=("TongDiem", "mean"),
    Max=("TongDiem", "max")
)

print("\nThống kê theo khu vực:")
print(thong_ke)

# ======================
# 7. Xuất file
# ======================
df.to_csv("tuyensinh_clean.csv", index=False)
thong_ke.to_csv("tuyensinh_thongke.csv")