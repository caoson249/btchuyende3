import numpy as np

scores = np.array([
[7.5, 8.0, 6.5, 9.0],
[6.0, 7.0, 7.5, 8.0],
[8.5, 9.0, 8.0, 9.5],
[5.5, 6.0, 6.5, 7.0],
[9.0, 8.5, 9.5, 8.0]
])

# 1. In ma trận điểm
print("1. Ma trận điểm:")
print(scores)

# 2. Điểm trung bình toàn bộ
avg_all = np.mean(scores)
print("2. Điểm trung bình toàn bộ:", avg_all)

# 3. Điểm trung bình từng sinh viên
avg_students = np.mean(scores, axis=1)
print("3. Điểm trung bình từng sinh viên:", avg_students)

# 4. Điểm trung bình từng môn
avg_subjects = np.mean(scores, axis=0)
print("4. Điểm trung bình từng môn:", avg_subjects)

# 5. Điểm cao nhất và thấp nhất
max_score = np.max(scores)
min_score = np.min(scores)
print("5. Điểm cao nhất:", max_score)
print("   Điểm thấp nhất:", min_score)

# 6. Độ lệch chuẩn từng môn
std_subjects = np.std(scores, axis=0)
print("6. Độ lệch chuẩn từng môn:", std_subjects)

# 7. Sinh viên có điểm trung bình cao nhất
best_student = np.argmax(avg_students)
print("7. Sinh viên có điểm trung bình cao nhất là vị trí:", best_student)