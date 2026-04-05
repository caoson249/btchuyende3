import pandas as pd


data = {
    "MaHD": ["HD01", "HD02", "HD03", "HD04", "HD05", "HD06", "HD07", "HD08", "HD09", "HD10", "HD11", "HD12"],
    "NhanVien": ["An", "Binh", "Chi", "An", "Dung", "Chi", "An", "Binh", "Dung", "Chi", "An", "Binh"],
    "SoLuong": [1, 5, 2, 3, 1, 4, 2, 6, 1, 2, 1, 3],
    "DonGia": [14500000, 150000, 2500000, 750000, 900000, 450000, 300000, 180000, 2500000, 900000, 14500000, 300000]
}

df = pd.DataFrame(data)
df["DoanhThu"] = df["SoLuong"] * df["DonGia"]

tong_nv = df.groupby("NhanVien")["DoanhThu"].sum().reset_index()
tong_nv = tong_nv.sort_values(by="DoanhThu", ascending=False)

print("Tong doanh thu cua tung nhan vien:")
print(tong_nv)

print("\nNhan vien doanh thu cao nhat:")
print(tong_nv.iloc[0])

print("\nNhan xet ngan:")
for _, row in tong_nv.iterrows():
    print(f"- {row['NhanVien']}: doanh thu {int(row['DoanhThu']):,} VND")
