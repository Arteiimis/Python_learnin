import math


def f(a):
    return math.pow(a, 2)


times = 10000000

riemannSum = 0

a = 1
b = 3
delta = (b - a) / times

for i in range(1, times + 1):
    riemannSum += delta * math.sin(a + i * delta)

print(riemannSum)
