# 导入 python 库
import numpy as np

# 创建函数
f = lambda x: 1 / (1 + x ** 2)
# 定义变量 #
a = 0
b = 5
N = 10000000
# 离散的 x 和对应的函数值 y
x = np.linspace(a, b, N + 1)
y = f(x)
# 计算黎曼和
dx = (b - a) / N
x_left = np.linspace(a, b - dx, N)
x_midpoint = np.linspace(dx / 2, b - dx / 2, N)
x_right = np.linspace(dx, b, N)
print("按划分为", N, "个子区间计算：")
left_riemann_sum = np.sum(f(x_left) * dx)
print("左黎曼和:", left_riemann_sum)
midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("中黎曼和:", midpoint_riemann_sum)
right_riemann_sum = np.sum(f(x_right) * dx)
print("右黎曼和:", right_riemann_sum)
