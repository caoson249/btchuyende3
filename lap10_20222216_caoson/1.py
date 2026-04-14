import pandas as pd
import numpy as np
import re

# ==============================
# TẠO DỮ LIỆU
# ==============================
data = [
["SV001", "Nguyen Van An", "CNTT 1", "Nam", "2004-01-12","an01@eaut.edu.vn", "0912345678", 8.5, 92, "Da nop"],
["SV002", "Tran Thi Binh", "CNTT1", "Nữ", "2004/03/04","binh02@eaut.edu.vn","0988123456", 7.2, 88, "Chua nop"],
["SV003", "Le Van Cuong", "CNTT 2", "nam", "12-07-2004","cuong03@email.com", None, 9.1, 95, "Da nop"],
["SV004", "Pham Thi Dung", "CNTT 2", None, "2004-05-21","dung04@email.com", "0912.567.890", 6.8, 79, "Da nop"],
["SV005", "Hoang Minh Duc", "CNTT-3", "Nam ", "2004-11-02","duc05@email.com", " 0977555333 ", 11.0, 85, "Da nop"],
["SV005", "Hoang Minh Duc", "CNTT-3", "Nam ", "2004-11-02","duc05@email.com", " 0977555333 ", 11.0, 85, "Da nop"],
["SV006", "Vu Thi Ha", "CNTT 3", "Nu", None, "ha06@email","0966888777", 5.4, 61, "Chua nop"],
["SV007", "Doan Quoc Huy", "CNTT 1", "NAM", "2004-08-16","huy07@email.com", "0933444555", -1.0, 98, "Da nop"],
["SV008", "Bui Thu Linh", "CNTT 2", "Nữ", "2004-09-30","linh08@email.com", "0944333222", 8.0, None, "Da nop"],
["SV009", "Nguyen Van Nam", "CNTT 1", "Nam", "2004-10-10","nam09@email.com", "0911112222", 7.9, 82, "Tre han"],
]

cols = ["student_id", "full_name", "class_name", "gender", "birth_date",
        "email", "phone", "score_python", "attendance_rate", "tuition_status"]

df = pd.DataFrame(data, columns=cols)
df.to_csv("student_performance_dirty.csv", index=False, encoding="utf-8-sig")

# ==============================
# BÀI 1
# ==============================
print("\n========== BÀI 1: ĐỌC DỮ LIỆU ==========")
df = pd.read_csv("student_performance_dirty.csv")
print(df.head())
print(df.info())
print(df.isna().sum())

# ==============================
# BÀI 2
# ==============================
print("\n========== BÀI 2: CHUẨN HÓA CLASS & GENDER ==========")

df["class_name"] = (
    df["class_name"]
    .str.replace("-", " ")
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
    .str.upper()
    .replace({"CNTT1": "CNTT 1","CNTT2": "CNTT 2","CNTT3": "CNTT 3"})
)

df["gender"] = (
    df["gender"]
    .astype("string")
    .str.strip()
    .str.lower()
    .replace({"nam": "Nam", "nữ": "Nữ", "nu": "Nữ"})
)

print(df[["class_name","gender"]].head())

# ==============================
# BÀI 3
# ==============================
print("\n========== BÀI 3: XỬ LÝ MISSING ==========")

df["gender"] = df["gender"].fillna("Không rõ")
df["attendance_rate"] = df["attendance_rate"].fillna(df["attendance_rate"].median())
df["phone"] = df["phone"].fillna("Chưa cập nhật")

print(df.isna().sum())

# ==============================
# BÀI 4
# ==============================
print("\n========== BÀI 4: XÓA TRÙNG ==========")

print("Trùng hoàn toàn:", df.duplicated().sum())
print("Trùng theo ID:", df.duplicated(subset=["student_id"]).sum())

df = df.drop_duplicates()
df = df.drop_duplicates(subset=["student_id"], keep="first")

# ==============================
# BÀI 5
# ==============================
print("\n========== BÀI 5: XỬ LÝ ĐIỂM ==========")

invalid = ~df["score_python"].between(0,10)
print(df.loc[invalid, ["student_id","score_python"]])

df.loc[invalid,"score_python"] = np.nan
df["score_python"] = df["score_python"].fillna(df["score_python"].median())

# ==============================
# BÀI 6
# ==============================
print("\n========== BÀI 6: CHUẨN HÓA CHUỖI ==========")

df["full_name"] = (
    df["full_name"]
    .str.replace(r"\s+"," ",regex=True)
    .str.strip()
    .str.title()
)

email_mask = df["email"].str.contains(r"^[\w\.-]+@[\w\.-]+\.\w+$", regex=True, na=False)
print("Email sai:")
print(df.loc[~email_mask, ["student_id","email"]])

df["phone"] = df["phone"].astype("string").str.replace(r"\D","",regex=True)

# ==============================
# BÀI 7
# ==============================
print("\n========== BÀI 7: XỬ LÝ NGÀY ==========")

df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce", dayfirst=True)
print("Ngày lỗi:", df["birth_date"].isna().sum())

# ==============================
# BÀI 8
# ==============================
print("\n========== BÀI 8: PHÂN NHÓM ==========")

bins = [0,5,6.5,8,10]
labels = ["Yếu","Trung bình","Khá","Giỏi"]

df["level"] = pd.cut(df["score_python"], bins=bins, labels=labels, include_lowest=True)
print(df[["student_id","score_python","level"]])

# ==============================
# BÀI 9
# ==============================
print("\n========== BÀI 9: OUTLIER ==========")

q1 = df["attendance_rate"].quantile(0.25)
q3 = df["attendance_rate"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outlier_df = df[(df["attendance_rate"] < lower) | (df["attendance_rate"] > upper)]
print(outlier_df[["student_id","attendance_rate"]])

# ==============================
# BÀI 10
# ==============================
print("\n========== BÀI 10: LƯU FILE ==========")

df.to_csv("student_performance_clean.csv", index=False, encoding="utf-8-sig")
print("Đã lưu file!")

# ==============================
# NHẬN XÉT
# ==============================
print("""
Nhận xét:
- Làm sạch dữ liệu thiếu
- Chuẩn hóa chuỗi
- Xóa trùng
- Xử lý điểm lỗi
- Chuẩn hóa ngày
- Phát hiện outlier
""")