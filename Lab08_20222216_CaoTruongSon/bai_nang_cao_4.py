from pathlib import Path

import pandas as pd


def load_data(file_path):
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix == ".xlsx":
        return pd.read_excel(path)
    if suffix == ".json":
        return pd.read_json(path)

    raise ValueError(f"Dinh dang file khong duoc ho tro: {suffix}")


base = Path(__file__).parent
test_files = [
    base / "students.csv",
    base / "inventory.xlsx",
    base / "products.json",
]

for file_path in test_files:
    df = load_data(file_path)
    print(f"\nFile: {file_path.name}")
    print(df.head())

print("\nHam load_data da doc thanh cong 3 dinh dang: CSV, XLSX, JSON.")
