import pandas as pd


data = {
    "MaHD": ["HD01", "HD02", "HD03", "HD04", "HD05", "HD06", "HD07", "HD08", "HD09", "HD10"],
    "NgayBan": [
        "2026-04-01", "2026-04-01", "2026-04-02", "2026-04-02", "2026-04-03",
        "2026-04-03", "2026-04-04", "2026-04-04", "2026-04-05", "2026-04-05"
    ],
    "TenSP": ["Laptop", "Chuot", "Man hinh", "USB", "Loa", "Tai nghe", "Laptop", "Webcam", "Ban phim", "Man hinh"],
    "SoLuong": [1, 5, 2, 10, 3, 4, 1, 2, 6, 1],
    "DonGia": [14500000, 150000, 2500000, 180000, 750000, 450000, 14500000, 900000, 300000, 2500000],
    "NhanVien": ["An", "Binh", "An", "Chi", "Dung", "Ha", "An", "Chi", "Binh", "Ha"]
}

df = pd.DataFrame(data)
df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

print("5 hoa don co gia tri cao nhat:")
print(df.sort_values(by="ThanhTien", ascending=False).head(5))

print("\nCac hoa don co ThanhTien >= 3000000:")
print(df[df["ThanhTien"] >= 3000000])

print("\nTong doanh thu:", df["ThanhTien"].sum())
