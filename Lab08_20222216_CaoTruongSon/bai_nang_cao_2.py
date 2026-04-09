from pathlib import Path

import pandas as pd


def chuan_hoa_ten_cot(df):
    mapping = {
        "OrderID": "MaDon",
        "Date": "NgayBan",
        "Customer": "KhachHang",
        "Product": "SanPham",
        "Quantity": "SoLuong",
        "UnitPrice": "DonGia",
        "Revenue": "DoanhThu",
        "id_don": "MaDon",
        "ngay": "NgayBan",
        "ten_khach": "KhachHang",
        "san_pham": "SanPham",
        "sl": "SoLuong",
        "gia": "DonGia",
        "thanh_tien": "DoanhThu",
    }
    return df.rename(columns=mapping)


base = Path(__file__).parent
files = ["sales_jan.csv", "sales_feb.csv", "sales_mar.csv"]

dataframes = []
for file_name in files:
    df = pd.read_csv(base / file_name)
    df = chuan_hoa_ten_cot(df)
    dataframes.append(df)

sales_q1 = pd.concat(dataframes, ignore_index=True)
sales_q1 = sales_q1[
    ["MaDon", "NgayBan", "KhachHang", "SanPham", "SoLuong", "DonGia", "DoanhThu"]
]

output_path = base / "sales_q1.csv"
sales_q1.to_csv(output_path, index=False)

print("Du lieu sau khi chuan hoa va gop 3 thang:")
print(sales_q1)
print("\nDa luu file:", output_path.name)
