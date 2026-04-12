import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/suckhoe.csv")

# 1. Phát hiện tuổi không hợp lệ
tuoi_loi = df[(df["Tuoi"] <= 0) | (df["Tuoi"] > 100)]
print("Tuổi không hợp lệ:")
print(tuoi_loi)

# 2. Phát hiện thiếu CanNang, ChieuCao
thieu = df[df["CanNang"].isna() | df["ChieuCao"].isna()]
print("\nDữ liệu thiếu:")
print(thieu)

# 3. Điền thiếu bằng trung vị
df["CanNang"] = df["CanNang"].fillna(df["CanNang"].median())
df["ChieuCao"] = df["ChieuCao"].fillna(df["ChieuCao"].median())

# 4. Chuẩn hóa NhomMau
df["NhomMau"] = df["NhomMau"].str.strip().str.upper()
df["NhomMau"] = df["NhomMau"].replace({
    "A": "A",
    "B": "B",
    "AB": "AB",
    "O": "O"
})

# 5. Tính BMI
df["BMI"] = df["CanNang"] / ((df["ChieuCao"] / 100) ** 2)

# Kết quả
print("\nDữ liệu sau xử lý:")
print(df)

# Lưu file nếu cần
df.to_csv("suckhoe_clean.csv", index=False)