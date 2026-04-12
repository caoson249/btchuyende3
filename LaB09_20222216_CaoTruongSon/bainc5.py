import pandas as pd
import numpy as np

# ======================
# 1. Đọc dữ liệu
# ======================
df = pd.read_csv("LaB09_20222216_CaoTruongSon/data.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

# ======================
# 2. Kiểm tra lỗi
# ======================
print("\n=== GIÁ TRỊ THIẾU ===")
print(df.isna().sum())

print("\n=== DỮ LIỆU TRÙNG ===")
print(df.duplicated().sum())

# ======================
# 3. Xử lý missing values
# ======================
df["Gender"] = df["Gender"].fillna("Không rõ")
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")

# ======================
# 4. Xóa trùng
# ======================
df = df.drop_duplicates()

# ======================
# 5. Chuẩn hóa dữ liệu
# ======================

# Chuẩn hóa tên
df["CustomerName"] = df["CustomerName"].str.strip().str.title()

# Chuẩn hóa giới tính
df["Gender"] = df["Gender"].str.strip().str.lower()
df["Gender"] = df["Gender"].replace({
    "nam": "Nam",
    "male": "Nam",
    "nữ": "Nữ",
    "nu": "Nữ",
    "female": "Nữ"
})

# Chuẩn hóa category
df["Category"] = df["Category"].str.strip().str.lower()

# Chuẩn hóa giá
df["Price"] = df["Price"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["Price"] = df["Price"].astype(float)

# ======================
# 6. Xử lý dữ liệu sai
# ======================
print("\n=== ĐƠN LỖI (Quantity <= 0) ===")
loi = df[df["Quantity"] <= 0]
print(loi)

df = df[df["Quantity"] > 0]

# ======================
# 7. Tạo biến mới
# ======================
df["Revenue"] = df["Quantity"] * df["Price"]
df["Month"] = df["OrderDate"].dt.month
df["NameLength"] = df["CustomerName"].str.len()

# ======================
# 8. Xử lý outlier (IQR)
# ======================
Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Revenue"] >= Q1 - 1.5*IQR) & (df["Revenue"] <= Q3 + 1.5*IQR)]

# ======================
# 9. Báo cáo
# ======================
print("\n=== DOANH THU THEO THÁNG ===")
print(df.groupby("Month")["Revenue"].sum())

print("\n=== TOP SẢN PHẨM ===")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

print("\n=== DOANH THU THEO DANH MỤC ===")
print(df.groupby("Category")["Revenue"].mean())

# ======================
# 10. Lưu file
# ======================
df.to_csv("clean_data.csv", index=False)

print("\n=== DỮ LIỆU SAU XỬ LÝ ===")
print(df)