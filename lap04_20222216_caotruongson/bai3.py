import numpy as np

# Dữ liệu doanh thu (7 ngày x 5 sản phẩm)
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

# 1. Tổng doanh thu theo từng ngày
daily_total = sales.sum(axis=1)
print("Tổng doanh thu từng ngày:")
print(daily_total)

# 2. Tổng và trung bình từng sản phẩm
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)
print("\nTổng doanh thu từng sản phẩm:")
print(product_total)
print("Doanh thu trung bình từng sản phẩm:")
print(np.round(product_mean, 2))

# 3. Ngày cao nhất & sản phẩm tốt nhất
best_day = np.argmax(daily_total)
best_product = np.argmax(product_total)
print("\nNgày doanh thu cao nhất: Ngày", best_day + 1)
print("Sản phẩm bán tốt nhất: Sản phẩm", best_product + 1)

# 4. Tăng 8% sản phẩm 2 và 5
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08
print("\nDoanh thu sau điều chỉnh (SP2 & SP5 tăng 8%):")
print(np.round(new_sales, 2))

# 5. So sánh tổng trước và sau
before_total = sales.sum()
after_total = new_sales.sum()
print("\nTổng trước:", before_total)
print("Tổng sau:", round(after_total, 2))
print("Chênh lệch:", round(after_total - before_total, 2))

# 6. Ngày có doanh thu > trung bình
high_days = np.where(daily_total > daily_total.mean())[0]
print("\nNgày doanh thu > trung bình:", high_days + 1)

# 7. Sản phẩm ổn định nhất (std nhỏ nhất)
stable_product = np.argmin(sales.std(axis=0))
print("\nSản phẩm ổn định nhất:", stable_product + 1)

# 8. Nhận xét
print("\nNhận xét:")
print("- Sản phẩm", best_product + 1, "có doanh thu cao nhất, nên ưu tiên bán.")
print("- Sản phẩm", stable_product + 1, "ổn định nhất, phù hợp chiến lược lâu dài.")
print("- Việc tăng giá/khuyến mãi SP2 và SP5 giúp tăng tổng doanh thu rõ rệt.")