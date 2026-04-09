from pathlib import Path

import pandas as pd


file_path = Path(__file__).with_name("sales_semicolon.csv")

print("Doc sai tham so sep mac dinh:")
df_sai = pd.read_csv(file_path)
print(df_sai.head())

print("\nDoc dung voi sep=';':")
df_dung = pd.read_csv(file_path, sep=";")
print(df_dung.head())

print(
    "\nGiai thich: neu chon sai dau phan tach, pandas khong tach duoc cac cot "
    "nen ca dong du lieu bi don vao mot cot duy nhat."
)
