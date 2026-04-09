from pathlib import Path

import pandas as pd


file_path = Path(__file__).with_name("products.json")
df = pd.read_json(file_path)

print(df[["MaSP", "TenSP", "NhomHang", "Gia"]])

print(
    "\nNhan xet: JSON linh hoat hon CSV vi co the luu du lieu theo cau truc "
    "phan cap, con CSV phu hop du lieu bang don gian theo hang va cot."
)
