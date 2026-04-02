import numpy as np

A = np.array([
[2,1],
[1,3]
])

B = np.array([
[4,2],
[1,5]
])

# 1. A + B
print("1. A + B =")
print(A + B)

# 2. A - B
print("2. A - B =")
print(A - B)

# 3. Tích ma trận A @ B
print("3. A @ B =")
print(A @ B)

# 4. Định thức của A
det_A = np.linalg.det(A)
print("4. det(A) =", det_A)

# 5. Ma trận nghịch đảo của A
inv_A = np.linalg.inv(A)
print("5. A^-1 =")
print(inv_A)

# 6. Giải hệ phương trình
b = np.array([5,7])
solution = np.linalg.solve(A, b)
print("6. Nghiệm hệ phương trình [x, y] =", solution)

# Kiểm tra lại nghiệm
check = A @ solution
print("Kiểm tra nghiệm A @ [x,y] =", check)

# Giải thích khi ma trận không khả nghịch
print("Ma trận không khả nghịch khi det(A) = 0.")