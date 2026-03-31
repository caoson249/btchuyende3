import numpy as np

# Dữ liệu
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

# 1 + 2. Xác định thiếu & số lượng cần nhập
need_import = np.maximum(min_stock - stock, 0)
print("Số lượng cần nhập thêm:")
print(need_import)

# 3. Chi phí nhập (chỉ tính hàng thiếu)
cost = need_import * price
print("\nChi phí nhập từng mặt hàng:")
print(cost)

# 4. Tổng chi phí
total_cost = cost.sum()
print("\nTổng chi phí nhập hàng:", total_cost)

# 5. Trạng thái hàng
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
print("\nTrạng thái từng mặt hàng:")
for i, s in enumerate(status):
    print(f"Mặt hàng {i+1}: {s}")

# 6. Top 3 thiếu nhiều nhất
top3_shortage = np.argsort(need_import)[::-1][:3]
print("\nTop 3 mặt hàng thiếu nhiều nhất:", top3_shortage + 1)

# 7. Giới hạn nhập tối đa 20
limited_need = np.clip(need_import, 0, 20)
print("\nSố lượng nhập sau khi giới hạn (max 20):")
print(limited_need)

# 8. Tổng chi phí sau giới hạn
limited_total_cost = (limited_need * price).sum()
print("\nTổng chi phí sau giới hạn:", limited_total_cost)

# 9. Nhận xét
print("\nNhận xét:")
print("- Kho đang thiếu ở nhiều mặt hàng, đặc biệt là các mặt hàng có tồn kho thấp.")
print("- Một số mặt hàng thiếu đáng kể cần ưu tiên nhập trước.")
print("- Việc giới hạn nhập giúp kiểm soát chi phí nhưng có thể chưa đáp ứng đủ nhu cầu.")