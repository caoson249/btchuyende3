import pandas as pd
import numpy as np

# ======================
# 1. Tạo dữ liệu ban đầu
# ======================
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 20, 2, 5, None],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None]
}

df = pd.DataFrame(data)

# ======================
# 2. Kiểm tra dữ liệu
# ======================
print("Dữ liệu ban đầu:\n", df)
print("Kích thước dữ liệu:", df.shape)
print("Dữ liệu thiếu:\n", df.isnull().sum())

# ======================
# 3. Xóa trùng lặp
# ======================
df = df.drop_duplicates(subset="MaSV")

# ======================
# 4. Chuẩn hóa giới tính
# ======================
df["GioiTinh"] = df["GioiTinh"].replace({
    "nu": "Nữ",
    "Nữ": "Nữ",
    "Nam": "Nam"
})
df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# ======================
# 5. Điền dữ liệu thiếu
# ======================
df["Tuoi"] = df["Tuoi"].fillna(df["Tuoi"].mean())
df["GioTuHoc"] = df["GioTuHoc"].fillna(df["GioTuHoc"].mean())
df["GioMangXaHoi"] = df["GioMangXaHoi"].fillna(df["GioMangXaHoi"].mean())
df["DiemTB"] = df["DiemTB"].fillna(df["DiemTB"].mean())

# ======================
# 6. Xử lý dữ liệu bất thường
# ======================
df.loc[df["Tuoi"] > 30, "Tuoi"] = df["Tuoi"].mean()
df.loc[df["GioTuHoc"] < 0, "GioTuHoc"] = df["GioTuHoc"].mean()
df.loc[df["GioMangXaHoi"] > 12, "GioMangXaHoi"] = df["GioMangXaHoi"].mean()
df.loc[df["DiemTB"] > 4.0, "DiemTB"] = df["DiemTB"].mean()

print("\nDữ liệu sau làm sạch:\n", df)

# ======================
# 7. Chuẩn hóa Min-Max
# ======================
cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]

df_minmax = df.copy()
for col in cols:
    df_minmax[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

print("\nDữ liệu Min-Max:\n", df_minmax)

# ======================
# 8. Chuẩn hóa Z-score
# ======================
df_zscore = df.copy()
for col in cols:
    df_zscore[col] = (df[col] - df[col].mean()) / df[col].std()

print("\nDữ liệu Z-score:\n", df_zscore)