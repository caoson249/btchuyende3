import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# BÀI 1
# ==============================
print("\n===== BÀI 1 =====")

df = pd.read_csv("time_series_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df = df.set_index("Date")

print(df.head(10))
print(df.index)

# ==============================
# BÀI 2 (ĐÃ SỬA LỖI)
# ==============================
print("\n===== BÀI 2 =====")

# 🔥 SỬA Ở ĐÂY: "M" → "ME"
monthly_data = df["Value"].resample("ME").sum()

print(monthly_data)

monthly_data.plot(figsize=(10, 5), title="Tong hop gia tri theo thang")
plt.show()

print("Tháng cao nhất:", monthly_data.idxmax())
print("Tháng thấp nhất:", monthly_data.idxmin())

# ==============================
# BÀI 3
# ==============================
print("\n===== BÀI 3 =====")

df["Lag_1"] = df["Value"].shift(1)
df["MA_3"] = df["Value"].rolling(3).mean()
df["MA_7"] = df["Value"].rolling(7).mean()

print(df.head(10))

# ==============================
# BÀI 4
# ==============================
print("\n===== BÀI 4 =====")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = df.dropna()

X = data[["Lag_1", "MA_3", "MA_7"]]
y = data["Value"]

split = int(len(data) * 0.8)

X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))

# ==============================
# BÀI 5
# ==============================
print("\n===== BÀI 5 =====")

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df_cluster = df.dropna().copy()

df_cluster["Feature1"] = df_cluster["Value"]
df_cluster["Feature2"] = df_cluster["MA_3"]

X = df_cluster[["Feature1", "Feature2"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=3, random_state=42)
df_cluster["Cluster"] = model.fit_predict(X_scaled)

plt.figure(figsize=(8,5))
plt.scatter(df_cluster["Feature1"], df_cluster["Feature2"], c=df_cluster["Cluster"])
plt.title("Phan cum KMeans")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()