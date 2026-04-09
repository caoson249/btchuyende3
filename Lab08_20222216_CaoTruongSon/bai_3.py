from pathlib import Path

import pandas as pd


file_path = Path(__file__).with_name("scores_no_header.csv")
df = pd.read_csv(
    file_path,
    header=None,
    names=["MaSV", "HoTen", "Lop", "DiemQT", "DiemThi"],
)

print(df.head())
print("\nThong tin du lieu:")
df.info()
