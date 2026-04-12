import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("LaB09_20222216_CaoTruongSon/moitruong.csv")

# 1. Tìm outlier bằng IQR
Q1 = df["NhietDo"].quantile(0.25)
Q3 = df["NhietDo"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# 2. Đánh dấu Outlier
df["Outlier"] = (df["NhietDo"] < lower) | (df["NhietDo"] > upper)

print("Dữ liệu trước xử lý:")
print(df)

# 3. Thay outlier bằng trung vị
median_temp = df["NhietDo"].median()
df.loc[df["Outlier"], "NhietDo"] = median_temp

# 4. Thống kê trước/sau
print("\nSố outlier:", df["Outlier"].sum())
print("Nhiệt độ trung vị:", median_temp)

print("\nDữ liệu sau xử lý:")
print(df)

# 5. Vẽ boxplot
plt.figure()
df["NhietDo"].plot(kind="box")
plt.title("Boxplot NhietDo sau khi xử lý")
plt.show()