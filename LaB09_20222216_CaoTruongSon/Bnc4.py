import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/reviews.csv")

# ======================
# 1. Xóa trùng
# ======================
df = df.drop_duplicates()

# ======================
# 2. Xử lý rating
# ======================
# Giữ rating hợp lệ 1–5
df.loc[(df["Rating"] < 1) | (df["Rating"] > 5), "Rating"] = None

# Điền lại bằng median
df["Rating"] = df["Rating"].fillna(df["Rating"].median())

# ======================
# 3. Làm sạch Comment
# ======================
df["Comment"] = df["Comment"].str.strip()

# Xóa ký tự lặp (ví dụ: kkkkk → kk)
df["Comment"] = df["Comment"].str.replace(r"(.)\1{2,}", r"\1\1", regex=True)

# ======================
# 4. Độ dài comment
# ======================
df["CommentLength"] = df["Comment"].str.len()

# ======================
# 5. Chuẩn hóa danh mục
# ======================
df["ProductCategory"] = df["ProductCategory"].str.strip().str.lower()

# ======================
# 6. Thống kê
# ======================
thong_ke = df.groupby("ProductCategory")["Rating"].mean()

print("Dữ liệu sau xử lý:")
print(df)

print("\nĐiểm trung bình theo danh mục:")
print(thong_ke)