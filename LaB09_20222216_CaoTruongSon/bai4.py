import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/muonsach.csv")

# 1. Chuyển về kiểu datetime
df["NgayMuon"] = pd.to_datetime(df["NgayMuon"])
df["NgayTra"] = pd.to_datetime(df["NgayTra"])

# 2. Giữ nguyên bản ghi chưa trả (NgayTra = NaN)
# (không cần xử lý gì thêm)

# 3. Chuẩn hóa TrangThai
df["TrangThai"] = df["TrangThai"].str.strip().str.lower()
df["TrangThai"] = df["TrangThai"].replace({
    "datra": "DaTra",
    "da tra": "DaTra",
    "chuatra": "ChuaTra",
    "chua tra": "ChuaTra"
})

# 4. Tính SoNgayMuon
df["SoNgayMuon"] = (df["NgayTra"] - df["NgayMuon"]).dt.days

# Nếu chưa trả thì tính đến hôm nay
today = pd.Timestamp.today()
df.loc[df["NgayTra"].isna(), "SoNgayMuon"] = (today - df["NgayMuon"]).dt.days

# 5. Liệt kê SV mượn quá 30 ngày
sv_qua_han = df[df["SoNgayMuon"] > 30]

print("Sinh viên mượn quá hạn:")
print(sv_qua_han[["MaSV", "TenSach", "SoNgayMuon"]])

# Lưu file nếu cần
df.to_csv("muonsach_clean.csv", index=False)