import pandas as pd


data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
    "HoTen": ["An", "Binh", "Chi", "Dung", "Ha"],
    "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1"],
    "DiemQT": [7.0, 8.5, 6.0, 9.0, 8.0],
    "DiemThi": [7.5, 8.0, 6.5, 9.5, 8.5]
}

df = pd.DataFrame(data)

print("DataFrame ban dau:")
print(df)

print("\nChon cot HoTen va DiemThi:")
print(df[["HoTen", "DiemThi"]])

df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

print("\nDataFrame sau khi them cot DiemTB:")
print(df)
