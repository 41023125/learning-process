import numpy as np
from scipy.optimize import curve_fit

# 定義要擬合的函數模型，例如一個二次方程
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# 提供數據點的 x 和 y 值
x_data = np.array([1, 2, 3, 4])
y_data = np.array([2, 3, 4, 5])

# 使用 curve_fit 函數進行擬合
params, params_covariance = curve_fit(quadratic_func, x_data, y_data)

# 從擬合結果中取得方程式的係數
a, b, c = params

# 打印方程式
equation = f"{a:.2f}x^2 + {b:.2f}x + {c:.2f}"
print("方程式：", equation)
