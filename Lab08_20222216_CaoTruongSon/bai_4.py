from pathlib import Path

import pandas as pd


file_path = Path(__file__).with_name("customers.csv")
df = pd.read_csv(file_path, dtype={"MaKH": str})

print(df)
print("\nKieu du lieu tung cot:")
print(df.dtypes)

print(
    "\nGiai thich: MaKH nen de kieu chuoi de tranh mat so 0 o dau "
    "va tranh bi coi la gia tri dung cho tinh toan."
)
