# 实现1-2+3-4+5...+99
m = 0
n = 1
while n <= 99:
    if n % 2 == 0:
        m = m - n
    else:
        m = m + n
    n += 1
    # sum(m)
print(m)
