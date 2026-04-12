import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/lienhe.csv")

# 1. Chuẩn hóa email về chữ thường
df["Email"] = df["Email"].str.lower()

# 2. Kiểm tra email hợp lệ
pattern_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
df["Email_HopLe"] = df["Email"].str.contains(pattern_email, regex=True)

# 3. Tách đầu số điện thoại (3 số đầu)
df["DauSo"] = df["SoDienThoai"].astype(str).str.extract(r"^(\d{3})")

# 4. Xóa khoảng trắng thừa trong địa chỉ
df["DiaChi"] = df["DiaChi"].str.strip()

# 5. Trích xuất domain email
df["Domain"] = df["Email"].str.extract(r"@([\w\.-]+)")

# Kết quả
print(df)