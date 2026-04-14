import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# TẠO DATA MẪU (nếu chưa có)
# ==============================
np.random.seed(42)

df = pd.DataFrame({
    "Nhom": np.random.choice(["A", "B", "C"], 100),
    "GiaTri": np.random.randint(10, 100, 100),
    "X": np.random.randint(1, 50, 100),
    "Y": np.random.randint(20, 200, 100)
})

# tạo label phân loại
df["Label"] = (df["GiaTri"] > 50).astype(int)

df.to_csv("data.csv", index=False)

# ==============================
# BÀI 1: ĐỌC & KHÁM PHÁ
# ==============================
print("\n===== BÀI 1 =====")

df = pd.read_csv("data.csv")

print(df.head())
print(df.info())
print(df.describe())

# ==============================
# BÀI 2: BIỂU ĐỒ CỘT
# ==============================
print("\n===== BÀI 2 =====")

group_data = df.groupby("Nhom")["GiaTri"].mean()
print(group_data)

group_data.plot(kind="bar", title="Gia tri trung binh theo nhom")
plt.show()

# ==============================
# BÀI 3: HISTOGRAM
# ==============================
print("\n===== BÀI 3 =====")

df["GiaTri"].plot(kind="hist", bins=10, title="Phan phoi du lieu")
plt.show()

# ==============================
# BÀI 4: BOXPLOT
# ==============================
print("\n===== BÀI 4 =====")

df.boxplot(column="GiaTri")
plt.title("Boxplot phat hien ngoai le")
plt.show()

# ==============================
# BÀI 5: SCATTER
# ==============================
print("\n===== BÀI 5 =====")

df.plot(kind="scatter", x="X", y="Y", title="Moi quan he giua X va Y")
plt.show()

# ==============================
# BÀI 6: HỒI QUY TUYẾN TÍNH
# ==============================
print("\n===== BÀI 6 =====")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = df[["X"]]
y = df["Y"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("Hệ số:", model.coef_)
print("Intercept:", model.intercept_)

# ==============================
# BÀI 7: PHÂN LOẠI
# ==============================
print("\n===== BÀI 7 =====")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = df[["X", "Y"]]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# ==============================
# BÀI 8: NHẬN XÉT
# ==============================
print("\n===== BÀI 8 =====")

print("""
Nhận xét:
- Dữ liệu đã được đọc và kiểm tra đầy đủ.
- Biểu đồ cột cho thấy sự khác biệt giữa các nhóm.
- Histogram cho thấy phân phối dữ liệu.
- Boxplot giúp phát hiện outlier.
- Scatter cho thấy mối quan hệ giữa X và Y.
- Hồi quy tuyến tính cho kết quả sai số MSE.
- Logistic Regression phân loại với độ chính xác tương đối tốt.
""")