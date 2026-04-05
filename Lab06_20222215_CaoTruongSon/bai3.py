import pandas as pd


df = pd.read_csv("diem_sinhvien.csv")

print("5 dong dau:")
print(df.head())

print("\n5 dong cuoi:")
print(df.tail())

print("\nThong tin du lieu:")
df.info()

print("\nThong ke mo ta:")
print(df.describe())

print("\nKich thuoc du lieu:", df.shape)
print("Ten cac cot:", df.columns.tolist())
