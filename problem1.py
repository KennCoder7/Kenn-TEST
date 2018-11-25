import numpy as np

t = 0
lx = 1.06
M = 16000
zj = 2000
m = [M * lx - 2000]
y = 0
for year in range(10):
    if (year >= 1) & (m[year - 1] > zj):
        m = np.append(m, m[year - 1] * lx - zj)
        y += 1

for i in range(y+1):
    print("# 第 %d 年交完租金后剩余 %0.2f 元" % (i + 1, m[i]))
