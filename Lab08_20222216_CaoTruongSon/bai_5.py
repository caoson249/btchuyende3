from pathlib import Path

import pandas as pd


utf8_path = Path(__file__).with_name("sinhvien_utf8.csv")
ansi_path = Path(__file__).with_name("sinhvien_ansi.csv")

print("Doc file UTF-8:")
df_utf8 = pd.read_csv(utf8_path, encoding="utf-8")
print(df_utf8)

print("\nThu doc file ANSI bang UTF-8:")
try:
    df_ansi_sai = pd.read_csv(ansi_path, encoding="utf-8")
    print(df_ansi_sai)
except UnicodeDecodeError as exc:
    print("Loi giai ma:", exc)

print("\nDoc lai file ANSI voi encoding phu hop:")
df_ansi_dung = pd.read_csv(ansi_path, encoding="cp1258")
print(df_ansi_dung)

print(
    "\nLuu y: voi du lieu khong dau, doc sai encoding co the van thay dung."
    " Tuy nhien voi du lieu co dau tieng Viet, chon sai encoding thuong gay loi "
    "hoac hien thi sai noi dung."
)
