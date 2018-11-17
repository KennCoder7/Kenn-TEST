import time
import sys
import numpy as np

i = np.arange(1, 5000)


def k_timer(bool_start_end, start_time):
    if bool_start_end:
        return time.time()
    else:
        print("# It takes %ds" % (time.time() - start_time))


def k_add(j):
    for n in range(len(j)):
        time.sleep(0.0001)
        j[n] = j[n] + 1
        sys.stdout.write("\r# Process: %0.1f%%" % (float(n) / float(len(j)) * 100))
    return j


start = k_timer(True, 0)    # 记录开始时间
k_add(i)
print('\n')
k_timer(False, start)   # 输出耗时
