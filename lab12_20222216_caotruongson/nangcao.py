import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ==============================
# ĐỌC DỮ LIỆU
# ==============================
df = pd.read_csv("time_series_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df = df.set_index("Date")

# ==============================
# TẠO FEATURE CHUNG
# ==============================
df["Lag_1"] = df["Value"].shift(1)
df["MA_3"] = df["Value"].rolling(3).mean()
df["MA_5"] = df["Value"].rolling(5).mean()
df["MA_7"] = df["Value"].rolling(7).mean()
df["MA_14"] = df["Value"].rolling(14).mean()

data = df.dropna()

# ==============================
# BÀI NÂNG CAO 1
# ==============================
print("\n===== BÀI NÂNG CAO 1 =====")

feature_sets = {
    "MA_3": ["Lag_1", "MA_3"],
    "MA_5": ["Lag_1", "MA_5"],
    "MA_7": ["Lag_1", "MA_7"],
    "MA_14": ["Lag_1", "MA_14"]
}

for name, features in feature_sets.items():
    X = data[features]
    y = data["Value"]

    split = int(len(data) * 0.8)

    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(name, "MSE =", mse)

print("=> MSE nhỏ nhất là mô hình tốt nhất")

# ==============================
# BÀI NÂNG CAO 2
# ==============================
print("\n===== BÀI NÂNG CAO 2 =====")

# dùng model cuối cùng (ví dụ MA_3)
X = data[["Lag_1", "MA_3"]]
y = data["Value"]

split = int(len(data) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)

# dự báo nhiều bước
last_value = data["Value"].iloc[-1]
future_preds = []

for i in range(5):
    pred = model.predict([[last_value, last_value]])[0]
    future_preds.append(pred)
    last_value = pred

print("Dự báo 5 bước tiếp theo:")
for i, v in enumerate(future_preds, 1):
    print(f"Bước {i}: {v}")

# ==============================
# BÀI NÂNG CAO 3
# ==============================
print("\n===== BÀI NÂNG CAO 3 =====")

y_pred = model.predict(X_test)

plt.figure(figsize=(10,5))
plt.plot(y_test.index, y_test.values, label="Thực tế")
plt.plot(y_test.index, y_pred, label="Dự đoán")
plt.title("So sánh thực tế và dự đoán")
plt.legend()
plt.show()

print("Nhận xét: đoạn nào 2 đường gần nhau → dự đoán tốt")

# ==============================
# BÀI NÂNG CAO 4
# ==============================
print("\n===== BÀI NÂNG CAO 4 =====")

trend_data = df.dropna().copy()
trend_data["TimeIndex"] = np.arange(len(trend_data))

X = trend_data[["TimeIndex"]]
y = trend_data["Value"]

model = LinearRegression()
model.fit(X, y)

trend_data["Trend"] = model.predict(X)

plt.figure(figsize=(10,5))
plt.plot(trend_data.index, trend_data["Value"], label="Giá trị gốc")
plt.plot(trend_data.index, trend_data["Trend"], label="Xu hướng")
plt.title("Phân tích xu hướng")
plt.legend()
plt.show()

print("Nhận xét: nếu đường trend đi lên → xu hướng tăng, ngược lại → giảm")

# ==============================
# BÀI NÂNG CAO 5 (MINI PROJECT)
# ==============================
print("\n===== BÀI NÂNG CAO 5 =====")

print("""
QUY TRÌNH:
1. Đọc dữ liệu và chuyển datetime
2. Làm sạch và sort theo thời gian
3. Tạo đặc trưng Lag + Moving Average
4. Trực quan hóa (line, trend)
5. Xây dựng mô hình Linear Regression
6. Đánh giá bằng MSE
7. Kết luận
""")

# train lại model tổng
X = data[["Lag_1", "MA_3", "MA_7"]]
y = data["Value"]

split = int(len(data)*0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))

print("""
KẾT LUẬN:
- Dữ liệu có xu hướng biến động theo thời gian.
- Moving Average giúp làm mượt dữ liệu.
- Mô hình dự báo có thể bám xu hướng nhưng chưa hoàn hảo.
- Có thể cải thiện bằng thêm feature hoặc dùng mô hình nâng cao hơn.
""")