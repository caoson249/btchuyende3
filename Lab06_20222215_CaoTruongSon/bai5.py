import pandas as pd


data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}

df = pd.DataFrame(data)
df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]


def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    if row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    return "Can ho tro"


df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

print("Bang du lieu khao sat:")
print(df)

print("\nSinh vien tu hoc > 2 gio/ngay va nghi <= 2 buoi:")
print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])

print("\nNhan xet ngan:")
print("1. Nhom Tich cuc thuong co DiemTB cao va so buoi nghi thap.")
print("2. So gio tu hoc tang co xu huong di kem DiemTB cao hon.")
print("3. Nhom Can ho tro tap trung o cac ban co gio tu hoc thap hoac nghi nhieu.")
print("4. Diem chuyen can va diem cuoi ky deu anh huong truc tiep den DiemTB.")
print("5. Cac sinh vien nghi <= 2 buoi va tu hoc > 2 gio co ket qua kha on dinh.")
print("6. Du lieu phu hop de tiep tuc phan tich tuong quan hoac hoi quy don gian.")
