import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/benhnhan.csv")

# ======================
# 1. Chuẩn hóa phân loại
# ======================

# Giới tính
df["GioiTinh"] = df["GioiTinh"].str.strip().str.lower()
df["GioiTinh"] = df["GioiTinh"].replace({
    "nam": "Nam",
    "male": "Nam",
    "nữ": "Nữ",
    "nu": "Nữ",
    "female": "Nữ"
})

# Chẩn đoán
df["ChanDoan"] = df["ChanDoan"].str.strip().str.title()

# ======================
# 2. Xử lý thiếu
# ======================

# Tuổi → median
df["Tuoi"] = df["Tuoi"].fillna(df["Tuoi"].median())

# Giới tính → mode
df["GioiTinh"] = df["GioiTinh"].fillna(df["GioiTinh"].mode()[0])

# Các chỉ số → median
for col in ["HuyetApTamThu", "HuyetApTamTruong", "DuongHuyet"]:
    df[col] = df[col].fillna(df[col].median())

# ======================
# 3. Xử lý outlier (IQR)
# ======================

for col in ["HuyetApTamThu", "HuyetApTamTruong", "DuongHuyet"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    median = df[col].median()

    df.loc[(df[col] < lower) | (df[col] > upper), col] = median

# ======================
# 4. Encode ChanDoan
# ======================

df["ChanDoan"] = df["ChanDoan"].map({
    "Binh Thuong": 0,
    "Cao Huyet Ap": 1,
    "Tieu Duong": 2
})

# ======================
# 5. Chuẩn hóa dữ liệu số
# ======================

scaler = MinMaxScaler()

cols = ["Tuoi", "HuyetApTamThu", "HuyetApTamTruong", "DuongHuyet"]
df[cols] = scaler.fit_transform(df[cols])

# ======================
# 6. Kết quả
# ======================
print(df)

# Lưu file
df.to_csv("benhnhan_ready.csv", index=False)