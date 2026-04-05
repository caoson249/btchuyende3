import pandas as pd


df = pd.read_csv("diem_sinhvien.csv")

print("Thong tin tong quan du lieu:")
df.info()

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

ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]
ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)

print("\nDanh sach sinh vien dat Kha tro len (sap xep giam dan theo DiemTB):")
print(ket_qua)

ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")
print("\nDa luu file ketqua_xuly.csv")
