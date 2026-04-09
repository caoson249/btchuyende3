from pathlib import Path

import pandas as pd


file_path = Path(__file__).with_name("students.csv")
df = pd.read_csv(file_path)

print("5 dong dau:")
print(df.head())

print("\nSo dong, so cot:", df.shape)
print("Ten cac cot:")
print(df.columns.tolist())
