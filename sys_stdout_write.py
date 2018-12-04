import sys
from time import sleep
import numpy as np

i = np.arange(1, 10000)
print(i)
# [   1    2    3 ... 9997 9998 9999]


def func(j):
    for n in range(len(j)):
        sleep(0.0001)
        j[n] = j[n] + 1
        # sys.stdout.write("\r# Process: %0.2f %%" % (float(n+1) / float(len(j)) * 100))
        print("\r# Process: %0.2f %%" % (float(n+1) / float(len(j)) * 100), end='')
    return j


i = func(i)
print("\n", i)
# Process: 100.0 %
#  [    2     3     4 ...  9998  9999 10000]