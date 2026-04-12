import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/chitieu.csv")

# 1. Kiểm tra giao dịch không hợp lệ
loi = df[df["SoTien"] <= 0]
print("Giao dịch lỗi:")
print(loi)

# 2. Loại bỏ dòng không hợp lệ
df = df[df["SoTien"] > 0]

# 3. Phân nhóm chi tiêu
bins = [0, 100000, 300000, float("inf")]
labels = ["Thấp", "Trung bình", "Cao"]

df["MucChiTieu"] = pd.cut(df["SoTien"], bins=bins, labels=labels)

# 4. Thống kê số giao dịch theo mức
thong_ke = df["MucChiTieu"].value_counts()
print("\nSố giao dịch theo mức:")
print(thong_ke)

# 5. Tổng chi tiêu theo nhóm
tong_chi = df.groupby("NhomChiTieu")["SoTien"].sum()
print("\nTổng chi theo nhóm:")
print(tong_chi)