from pathlib import Path
import sqlite3

import pandas as pd


db_path = Path(__file__).with_name("shop.db")
connection = sqlite3.connect(db_path)

df = pd.read_sql("SELECT * FROM orders", connection)

print("5 ban ghi dau:")
print(df.head())

print("\nTong so don hang:", len(df))
print("Tong doanh thu:", df["TongTien"].sum())

connection.close()
