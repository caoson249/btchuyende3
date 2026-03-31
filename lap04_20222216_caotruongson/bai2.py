import numpy as np

# Dữ liệu chuyên cần (1: có mặt, 0: vắng)
attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

# 1. Tổng số buổi đi học
present_count = attendance.sum(axis=1)
print("Số buổi đi học từng SV:")
print(present_count)

# 2. Tỉ lệ chuyên cần (%)
rate = present_count / attendance.shape[1] * 100
print("\nTỉ lệ chuyên cần (%):")
print(np.round(rate, 2))

# 3. SV bị cảnh báo (<75%)
warning_idx = np.where(rate < 75)[0]
print("\nSV bị cảnh báo (<75%):", warning_idx + 1)

# 4. Buổi vắng nhiều nhất
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session)
print("\nSố SV vắng từng buổi:")
print(absent_count_by_session)
print("Buổi vắng nhiều nhất: Buổi", worst_session + 1)

# 5. SV đi học đầy đủ
full_attendance = np.where(np.all(attendance == 1, axis=1))[0]
print("\nSV đi học đầy đủ:", full_attendance + 1)

# 6. SV có >= 2 buổi vắng liên tiếp
two_absent_in_row = np.where(
    np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1)
)[0]
print("SV vắng >= 2 buổi liên tiếp:", two_absent_in_row + 1)

# 7. Nhận xét
print("\nNhận xét:")
print("- Đa số sinh viên có ý thức học tập khá tốt.")
print("- Tuy nhiên vẫn có một số sinh viên vắng nhiều hoặc vắng liên tiếp.")
print("- Lớp có sự phân hóa về mức độ chuyên cần.")
print("- Cần nhắc nhở các sinh viên bị cảnh báo để cải thiện.")