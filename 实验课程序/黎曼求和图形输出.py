# 导入 python 库
import numpy as np
import matplotlib.pyplot as plt  # 创建函数

f = lambda x: 1 / (1 + x ** 2)
# 定义变量
a = 0
b = 5
N = 20
n = 20      # Use n*N+1 points to plot the function smoothly
x = np.linspace(a, b, N + 1)        # 离散的 x 和对应的函数值 y
y = f(x)
X = np.linspace(a, b, n * N + 1)        # 离散的 X 和对应的函数值 Y
Y = f(X)
# 做图代码
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(X, Y, 'g')
x_left = x[:-1]  # Left endpoints
y_left = y[:-1]
plt.plot(x_left, y_left, 'g.', markersize=10)
plt.bar(x_left, y_left, width=(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Left Riemann Sum, N = {}'.format(N))
plt.subplot(1, 3, 2)
plt.plot(X, Y, 'g')
x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid, y_mid, 'g.', markersize=10)
plt.bar(x_mid, y_mid, width=(b - a) / N, alpha=0.2, edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))
plt.subplot(1, 3, 3)
plt.plot(X, Y, 'g')
x_right = x[1:]  # Left endpoints
y_right = y[1:]
plt.plot(x_right, y_right, 'g.', markersize=10)
plt.bar(x_right, y_right, width=-(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Right Riemann Sum, N = {}'.format(N))
plt.savefig('D:\\test.png')
plt.show()
