import pandas as pd
import numpy as np

# ===== 1. Tạo dữ liệu mẫu =====
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
    "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D", "Hoang Van E"],
    "DiemQT": [8.0, 7.5, 9.0, 6.5, 8.2],
    "DiemGK": [7.5, 6.8, 8.5, 7.0, 8.0],
    "DiemCK": [8.5, 7.0, 9.2, 6.8, 8.7]
}

df = pd.DataFrame(data)

# ===== 2. Tính điểm trung bình =====
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# ===== 3. Hàm xếp loại =====
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

# ===== 4. Áp dụng cho cột DiemTB =====
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# ===== 5. Hiển thị kết quả =====
print(df[["MaSV", "HoTen", "DiemTB", "XepLoai"]])