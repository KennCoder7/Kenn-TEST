import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import pi

NX = 1024
temp = [0] * NX
txb = [0] * NX
c = [0] * NX

p = 0  # 相位
f = 100  # 频率
v = 100  # 幅值
q = 1  # 谐波次数

t = int(f/25)  # t为NX个点的半周期数， 假设额定频率为50Hz
for i in range(t):
    if i % 2 == 0:
        k = 1
    else:
        k = -1
    for j in range(int(NX*i/t), int(NX*(i+1)/t)):
        if NX*i/t <= j <= NX*i/t+NX/4/t:
            temp[j] = 4 * k * v * (j * t / 1.0 / NX - i)
        elif NX*i/t+NX/4/t <= j <= NX*i/t+NX*3/4/t:
            temp[j] = k * v
        else:
            temp[j] = 4 * k * v * (i + 1 - j * t / 1.0 / NX)

for i in range(NX):
    txb[i] = temp[int(i + p * NX / t / 180) % NX]

for i in range(NX):
    c[i] = 16 * 1.0 * v / pi / pi * (1 / q / q * sin(q * pi / 4.0) * sin(q * 2 * pi * f * i / 1024))

plt.plot(txb)
plt.title("Trapezoidal")
plt.grid(True)
plt.xlim(0, 1024)
plt.show()

plt.plot(c)
plt.title("Harmonic")
plt.grid(True)
plt.xlim(0, 1024)
plt.show()