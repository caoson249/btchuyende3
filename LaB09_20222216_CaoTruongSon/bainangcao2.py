import pandas as pd

# ======================
# 1. Đọc dữ liệu
# ======================
df1 = pd.read_csv("LaB09_20222216_CaoTruongSon/nangcao2/banhang_thang1.csv")
df2 = pd.read_csv("LaB09_20222216_CaoTruongSon/nangcao2/banhang_thang2.csv")
df3 = pd.read_csv("LaB09_20222216_CaoTruongSon/nangcao2/banhang_thang3.csv")

# ======================
# 2. Chuẩn hóa tên cột
# ======================
df2 = df2.rename(columns={
    "OrderID": "MaDon",
    "Product": "TenSP",
    "Date": "NgayDat",
    "Quantity": "SoLuong",
    "Price": "Gia"
})

# ======================
# 3. Ghép dữ liệu
# ======================
df = pd.concat([df1, df2, df3], ignore_index=True)

# ======================
# 4. Làm sạch dữ liệu
# ======================

# Chuẩn hóa ngày
df["NgayDat"] = pd.to_datetime(df["NgayDat"], errors="coerce")

# Chuẩn hóa giá (xóa ký tự tiền)
df["Gia"] = df["Gia"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["Gia"] = df["Gia"].astype(float)

# Loại bỏ đơn lỗi (số lượng <= 0)
loi = df[df["SoLuong"] <= 0]
print("Đơn lỗi:")
print(loi)

df = df[df["SoLuong"] > 0]

# ======================
# 5. Xử lý trùng đơn
# ======================
df = df.drop_duplicates(subset=["MaDon"], keep="first")

# ======================
# 6. Tính doanh thu
# ======================
df["DoanhThu"] = df["SoLuong"] * df["Gia"]

# ======================
# 7. Thêm cột tháng
# ======================
df["Thang"] = df["NgayDat"].dt.month

# ======================
# 8. Báo cáo
# ======================

# Doanh thu theo tháng
doanh_thu_thang = df.groupby("Thang")["DoanhThu"].sum()

# Top 5 sản phẩm
top_sp = df.groupby("TenSP")["DoanhThu"].sum().sort_values(ascending=False).head(5)

# Số đơn lỗi
so_don_loi = len(loi)

# ======================
# 9. In kết quả
# ======================
print("\nDoanh thu theo tháng:")
print(doanh_thu_thang)

print("\nTop 5 sản phẩm:")
print(top_sp)

print("\nSố đơn lỗi:", so_don_loi)