import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/sanpham.csv")

# 1. Loại bỏ ký tự tiền tệ và dấu phẩy
df["Gia"] = df["Gia"].astype(str).str.replace(r"[^\d]", "", regex=True)

# 2. Chuyển sang số
df["Gia"] = df["Gia"].astype(float)

# 3. Chuẩn hóa DanhMuc
df["DanhMuc"] = df["DanhMuc"].str.strip().str.lower()

# 4. Loại bỏ sản phẩm tồn kho < 0
df = df[df["SoLuongTon"] >= 0]

# 5. Sắp xếp theo giá giảm dần
df = df.sort_values(by="Gia", ascending=False)

# Kết quả
print(df)

# Lưu file nếu cần
df.to_csv("sanpham_clean.csv", index=False)