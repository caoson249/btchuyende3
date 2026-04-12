import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/donhang.csv")

# 1. Kiểm tra dòng trùng toàn bộ
print("Số dòng trùng toàn bộ:", df.duplicated().sum())

# 2. Kiểm tra trùng theo MaDon
print("Số MaDon bị trùng:", df.duplicated(subset=["MaDon"]).sum())

# 3. Xóa trùng (giữ bản ghi đầu tiên)
df = df.drop_duplicates(keep="first")
df = df.drop_duplicates(subset=["MaDon"], keep="first")

# 4. Tạo cột ThanhTien
df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

# 5. Sắp xếp theo NgayDat tăng dần
df = df.sort_values(by="NgayDat")

# Hiển thị kết quả
print(df.head())

# Lưu file mới
df.to_csv("donhang_clean.csv", index=False)