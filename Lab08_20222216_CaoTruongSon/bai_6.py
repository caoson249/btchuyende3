from pathlib import Path
import pandas as pd

file_path = Path(__file__).with_name("inventory.xlsx")

df = pd.read_excel(file_path, sheet_name="HangHoa", engine="openpyxl")

print("10 dong dau:")
print(df.head(10))

ton_kho_thap = df[df["SoLuongTon"] < 20]

print("\nMat hang co ton kho duoi 20:")
print(ton_kho_thap)