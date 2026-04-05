import pandas as pd


df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]


def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    if diem >= 7.0:
        return "Kha"
    if diem >= 5.5:
        return "Trung binh"
    return "Yeu"


df["XepLoai"] = df["DiemTB"].apply(xep_loai)

print("Sinh vien co DiemTB >= 8:")
print(df[df["DiemTB"] >= 8])

df = df.rename(columns={"HoTen": "TenSinhVien"})
df = df.set_index("MaSV")

print("\nDataFrame sau khi doi ten cot va dat index:")
print(df)
