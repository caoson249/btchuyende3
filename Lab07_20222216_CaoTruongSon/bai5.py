import pandas as pd
import numpy as np

# ===== TẠO DỮ LIỆU =====
data = {
    "MaSV": ["SV01","SV02","SV03","SV04","SV05","SV06","SV07","SV08"],
    "HoTen": ["A","B","C","D","E","F","G","H"],
    "GioiTinh": ["Nam","Nu","Nam","Nu","Nam","Nu","Nam","Nu"],
    "Lop": ["CNTT1","CNTT1","CNTT2","CNTT2","CNTT1","CNTT2","CNTT1","CNTT2"],
    "ChuyenNganh": ["CNTT","CNTT","HTTT","HTTT","CNTT","HTTT","CNTT","HTTT"],
    "DiemQT": [8,7,9,6,8,7,6,9],
    "DiemGK": [7,6.5,8.5,7,8,7.5,6,9],
    "DiemCK": [8.5,7,9,6.5,8.5,7,6.5,9]
}

df = pd.DataFrame(data)

# ===== TÍNH ĐIỂM TB + XẾP LOẠI =====
df["DiemTB"] = 0.2*df["DiemQT"] + 0.3*df["DiemGK"] + 0.5*df["DiemCK"]

def xep_loai(d):
    if d >= 8.5: return "A"
    elif d >= 7: return "B"
    elif d >= 5.5: return "C"
    elif d >= 4: return "D"
    else: return "F"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# ================= BÀI 5 =================
print("\n===== BÀI 5: THỐNG KÊ TẦN SUẤT =====")
print("Giới tính:\n", df["GioiTinh"].value_counts())
print("Lớp:\n", df["Lop"].value_counts())
print("Chuyên ngành:\n", df["ChuyenNganh"].value_counts())
print("Xếp loại:\n", df["XepLoai"].value_counts())

# ================= BÀI 6 =================
print("\n===== BÀI 6: TB THEO LỚP =====")
print(df.groupby("Lop")["DiemTB"].mean())

# ================= BÀI 7 =================
print("\n===== BÀI 7: TB THEO GIỚI TÍNH =====")
print(df.groupby("GioiTinh")["DiemTB"].mean())

# ================= BÀI 8 =================
print("\n===== BÀI 8: TỔNG HỢP THEO LỚP =====")
print(df.groupby("Lop")["DiemTB"].agg(["count","mean","max","min"]))

# ================= BÀI 9 =================
print("\n===== BÀI 9: THEO LỚP + GIỚI TÍNH =====")
print(df.groupby(["Lop","GioiTinh"])["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
))

# ================= BÀI 10 =================
print("\n===== BÀI 10: PIVOT TABLE =====")
pivot1 = pd.pivot_table(df, index="Lop", columns="XepLoai",
                        values="MaSV", aggfunc="count", fill_value=0)
print(pivot1)

# ================= BÀI 11 =================
print("\n===== BÀI 11: CROSSTAB =====")
print(pd.crosstab(df["Lop"], df["GioiTinh"]))

# ================= BÀI 12 =================
print("\n===== BÀI 12: NHÓM ĐIỂM =====")
bins = [0,5,7,8.5,10]
labels = ["<5","5-6.9","7-8.4",">=8.5"]
df["NhomDiem"] = pd.cut(df["DiemTB"], bins=bins, labels=labels, right=False)
print(pd.crosstab(df["Lop"], df["NhomDiem"]))

# ================= BÀI 13 =================
print("\n===== BÀI 13: XẾP HẠNG =====")
df["XepHangTrongLop"] = df.groupby("Lop")["DiemTB"].rank(ascending=False, method="dense")
print(df[["HoTen","Lop","DiemTB","XepHangTrongLop"]]
      .sort_values(["Lop","XepHangTrongLop"]))

# ================= BÀI 14 =================
print("\n===== BÀI 14: SV CAO NHẤT MỖI LỚP =====")
idx = df.groupby("Lop")["DiemTB"].idxmax()
print(df.loc[idx, ["HoTen","Lop","DiemTB"]])

# ================= BÀI 15 =================
print("\n===== BÀI 15: ĐỖ / TRƯỢT =====")
df["KetQua"] = np.where(df["DiemTB"] >= 4, "Do", "Truot")

so_luong = pd.crosstab(df["Lop"], df["KetQua"])
print("Số lượng:\n", so_luong)

ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index")
print("\nTỷ lệ:\n", ty_le)

# ================= BÀI 16 =================
print("\n===== BÀI 16: BÁO CÁO THEO CHUYÊN NGÀNH =====")

# Tổng hợp cơ bản
tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)

# Số sinh viên đạt A hoặc B
tyle_ab = df[df["XepLoai"].isin(["A", "B"])].groupby("ChuyenNganh")["MaSV"].count()

# Gộp vào bảng
tong_hop_cn["SoDatAB"] = tyle_ab

# Nếu ngành nào không có A/B thì = 0
tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)

# Tính tỷ lệ %
tong_hop_cn["TyLeDatAB"] = tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"] * 100

# In kết quả
print(tong_hop_cn.round(2))