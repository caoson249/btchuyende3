students = []

# Đọc file
with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = line.strip().split(",")
        ma_sv = data[0]
        ten = data[1]
        diem = float(data[2])

        students.append((ma_sv, ten, diem))

# In danh sách
print("Danh sách sinh viên:")
for sv in students:
    print(sv)

# Tìm điểm cao nhất
max_sv = max(students, key=lambda x: x[2])
print("\nSinh viên cao điểm nhất:", max_sv)

# Điểm trung bình
diem_tb = sum(sv[2] for sv in students) / len(students)
print("Điểm trung bình:", round(diem_tb, 2))

# Sinh viên >= 8
print("\nSinh viên điểm >= 8:")
for sv in students:
    if sv[2] >= 8:
        print(sv)