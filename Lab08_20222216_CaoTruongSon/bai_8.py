from pathlib import Path

import pandas as pd


nguong_doanh_thu = 1000000
file_path = Path(__file__).with_name("sales.csv")
df = pd.read_csv(file_path)

high_sales = df[df["DoanhThu"] > nguong_doanh_thu]

csv_path = Path(__file__).with_name("high_sales.csv")
excel_path = Path(__file__).with_name("high_sales.xlsx")

high_sales.to_csv(csv_path, index=False)
high_sales.to_excel(excel_path, index=False)

print("Cac don hang co doanh thu lon hon nguong:")
print(high_sales)
print("\nDa ghi ra file:")
print(csv_path.name)
print(excel_path.name)
