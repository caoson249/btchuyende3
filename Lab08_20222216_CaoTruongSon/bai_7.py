from pathlib import Path

import pandas as pd


file_path = Path(__file__).with_name("inventory.xlsx")
sheets = ["HangHoa", "NhapKho", "XuatKho"]

for sheet_name in sheets:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(f"\nSheet: {sheet_name}")
    print(df.head())
    print("Thong tin cau truc:")
    df.info()

print("\nMo ta chuc nang:")
print("- HangHoa: danh muc mat hang va thong tin ton kho hien tai.")
print("- NhapKho: luu cac phieu nhap hang vao kho.")
print("- XuatKho: luu cac phieu xuat hang ra kho.")
