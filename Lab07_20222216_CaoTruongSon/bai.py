import pandas as pd
import numpy as np

# ===== 1. Tạo dữ liệu mẫu =====
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
    "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D", "Hoang Van E"],
    "DiemQT": [8.0, 7.5, 9.0, 6.5, 8.2],   # Quá trình
    "DiemGK": [7.5, 6.8, 8.5, 7.0, 8.0],   # Giữa kỳ
    "DiemCK": [8.5, 7.0, 9.2, 6.8, 8.7]    # Cuối kỳ
}

df = pd.DataFrame(data)

# ===== 2. Tính điểm trung bình =====
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# ===== 3. Hiển thị kết quả =====
print(df[["MaSV", "HoTen", "DiemTB"]])