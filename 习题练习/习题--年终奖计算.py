"""
净利润计算年终奖示例
"""
i = int(input("请输入净利润："))

arr = [100000, 200000, 400000, 600000, 1000000, 0]
rat = [0.1, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for item in range(0, 6):
    if i > arr[item]:
        r += (i - arr[item]) * rat[item]
        print((i - arr[item]) * rat[item])
        i = arr[item]
print(r)