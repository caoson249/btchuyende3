import numpy as np

# Dữ liệu điểm
scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

weights = np.array([0.1, 0.2, 0.3, 0.4])

# 1. Thông tin ma trận
print("Shape:", scores.shape)
print("Số chiều (ndim):", scores.ndim)
print("Kiểu dữ liệu:", scores.dtype)

# 2. Điểm tổng kết
final_score = scores @ weights
print("\nĐiểm tổng kết:")
print(np.round(final_score, 2))

# 3. Xếp loại
def classify(x):
    if x >= 8.5:
        return 'A'
    elif x >= 7.0:
        return 'B'
    elif x >= 5.5:
        return 'C'
    else:
        return 'D'

rank = [classify(x) for x in final_score]
print("\nXếp loại:")
for i, r in enumerate(rank):
    print(f"Sinh viên {i+1}: {r}")

# 4. Cao nhất & thấp nhất
max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)
print("\nCao nhất: SV", max_idx + 1, "- Điểm:", round(final_score[max_idx], 2))
print("Thấp nhất: SV", min_idx + 1, "- Điểm:", round(final_score[min_idx], 2))

# 5. SV có điểm >= 7.0
good_sv = np.where(final_score >= 7.0)[0]
print("\nSV có điểm >= 7.0:", good_sv + 1)

# 6. SV có ít nhất 1 điểm < 5
low_component = np.any(scores < 5.0, axis=1)
print("SV có điểm thành phần < 5:", np.where(low_component)[0] + 1)

# 7. Sắp xếp & top 3
rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3]
print("\nXếp hạng giảm dần:", rank_idx + 1)
print("Top 3 sinh viên:", top3 + 1)

# 8. Z-score điểm cuối kỳ
z_final_exam = (scores[:, 3] - scores[:, 3].mean()) / scores[:, 3].std()
print("\nZ-score điểm cuối kỳ:")
print(np.round(z_final_exam, 2))

# Nhận xét
print("\nNhận xét:")
print("- Điểm có sự phân hóa tương đối rõ.")
print("- Có sinh viên vượt trội và sinh viên thấp hơn trung bình.")
print("- Phân bố điểm khá đều quanh giá trị trung bình.")