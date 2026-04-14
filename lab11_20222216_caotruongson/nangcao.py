import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    mean_squared_error, r2_score,
    accuracy_score, confusion_matrix, classification_report
)

# ==============================
# TẠO DATA (nếu chưa có)
# ==============================
np.random.seed(42)

df = pd.DataFrame({
    "X1": np.random.randint(1, 50, 120),
    "X2": np.random.randint(10, 100, 120),
    "X3": np.random.randint(5, 80, 120)
})

df["Y"] = df["X1"] * 2 + df["X2"] * 0.5 + np.random.randn(120) * 10
df["Label"] = (df["Y"] > df["Y"].mean()).astype(int)

df.to_csv("data.csv", index=False)

# ==============================
# BÀI NÂNG CAO 1
# ==============================
print("\n===== BÀI NÂNG CAO 1 =====")

df = pd.read_csv("data.csv")

# 1 biến
X1 = df[["X1"]]
y = df["Y"]

X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.2, random_state=42)

model1 = LinearRegression()
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

mse1 = mean_squared_error(y_test, pred1)
print("MSE (1 biến):", mse1)

# nhiều biến
X_multi = df[["X1", "X2", "X3"]]

X_train, X_test, y_train, y_test = train_test_split(X_multi, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

mse2 = mean_squared_error(y_test, pred2)
print("MSE (nhiều biến):", mse2)

print("=> Mô hình tốt hơn:", "Nhiều biến" if mse2 < mse1 else "1 biến")

# ==============================
# BÀI NÂNG CAO 2
# ==============================
print("\n===== BÀI NÂNG CAO 2 =====")

plt.figure()
plt.plot(y_test.values, label="Thực tế")
plt.plot(pred2, label="Dự đoán")
plt.title("Thực tế vs Dự đoán")
plt.legend()
plt.show()

print("Nhận xét: Hai đường càng gần nhau → mô hình càng tốt")

# ==============================
# BÀI NÂNG CAO 3
# ==============================
print("\n===== BÀI NÂNG CAO 3 =====")

corr = df.corr(numeric_only=True)
print(corr)

plt.figure(figsize=(8,6))
plt.imshow(corr, interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Ma tran tuong quan")
plt.tight_layout()
plt.show()

print("\nTương quan với Y:")
print(corr["Y"].sort_values(ascending=False))

# ==============================
# BÀI NÂNG CAO 4
# ==============================
print("\n===== BÀI NÂNG CAO 4 =====")

X = df[["X1", "X2"]]
y = df["Y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Linear
lr = LinearRegression()
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)

# Decision Tree
tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)
pred_tree = tree.predict(X_test)

print("Linear - MSE:", mean_squared_error(y_test, pred_lr))
print("Linear - R2:", r2_score(y_test, pred_lr))

print("Tree - MSE:", mean_squared_error(y_test, pred_tree))
print("Tree - R2:", r2_score(y_test, pred_tree))

# ==============================
# BÀI NÂNG CAO 5
# ==============================
print("\n===== BÀI NÂNG CAO 5 =====")

X = df[["X1", "X2", "X3"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# chưa chuẩn hóa
model_raw = LogisticRegression(max_iter=1000)
model_raw.fit(X_train, y_train)
pred_raw = model_raw.predict(X_test)

print("Accuracy chưa chuẩn hóa:", accuracy_score(y_test, pred_raw))

# chuẩn hóa
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model_scaled = LogisticRegression(max_iter=1000)
model_scaled.fit(X_train_s, y_train)
pred_scaled = model_scaled.predict(X_test_s)

print("Accuracy sau chuẩn hóa:", accuracy_score(y_test, pred_scaled))

# ==============================
# BÀI NÂNG CAO 6
# ==============================
print("\n===== BÀI NÂNG CAO 6 =====")

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==============================
# BÀI NÂNG CAO 7
# ==============================
print("\n===== BÀI NÂNG CAO 7 =====")

# 1. khám phá
print(df.describe())

# 2. biểu đồ
df["X1"].plot(kind="hist", title="Phân phối X1")
plt.show()

df.boxplot(column="X2")
plt.title("Boxplot X2")
plt.show()

df.plot(kind="scatter", x="X1", y="Y", title="X1 vs Y")
plt.show()

df.groupby("Label")["Y"].mean().plot(kind="bar", title="Trung bình Y theo Label")
plt.show()

# 3. mô hình đơn giản
X = df[["X1", "X2"]]
y = df["Y"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, pred))

print("""
KẾT LUẬN:
- Dữ liệu đã được khám phá và trực quan hóa.
- Các biến X1, X2 có ảnh hưởng đến Y.
- Mô hình Linear Regression cho kết quả dự đoán tương đối tốt.
- Có thể cải thiện bằng thêm dữ liệu hoặc chọn đặc trưng tốt hơn.
""")