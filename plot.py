from pick_arange import pick_arange
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 30)
y1 = pick_arange(np.arange(10, 50), 30)
x2 = pick_arange(np.arange(0, 30), 10)
y2 = pick_arange(np.arange(0, 60), 10)
# print(x1, y1)
# print(x2, y2)
# plt.plot(x1, y1, 'b')
# plt.plot(x1, y1, 'bo')
# plt.xticks(x1, rotation=90)
# plt.plot(x2, y2, 'g')
# plt.plot(x2, y2, 'go')
# plt.title("Kenn Plot")
# plt.xlabel("x")
# plt.ylabel("y")
# # plt.grid(True)  # 网线
# plt.show()

# plt.plot(x1, y1, 'b')
# plt.plot(x2, y2, 'g')


y = np.random.uniform(0, 1, 10)
plt.bar(np.arange(len(y)), y)
plt.bar(np.arange(len(y)), y/2)
plt.grid(True)
plt.show()
