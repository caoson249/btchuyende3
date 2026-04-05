import pandas as pd


diem = pd.Series(
    [7.5, 8.0, 6.5, 9.0, 8.5],
    index=["SV01", "SV02", "SV03", "SV04", "SV05"]
)

print("Danh sach diem:")
print(diem)

print("\nHai phan tu dau:")
print(diem.head(2))

print("\nDiem lon nhat:", diem.max())
print("Diem trung binh:", diem.mean())

print("\nSinh vien co diem >= 8:")
print(diem[diem >= 8])
