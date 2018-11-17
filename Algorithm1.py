import numpy as np

SI = np.array([], dtype=int)
for i in range(5):
    SI = np.append(SI, i+1)
print(SI)   # [1 2 3 4 5]

people = ['Kenn', 'Tom', 'Jerry', 'Jenifer', 'Candy']


def not_exist(arr, array):
    for i in range(len(array)):
        if arr[0] == array[i]:
            if i != len(array)-1:
                if arr[1] == array[i+1]:
                    return False
    return True


def algorithm1_real(SI):
    SIS = [1]
    SI_new = [SI[0]]
    i = 1
    j = i + 1
    while i != j:
        if j > len(SI):
            j = 1
        elif not_exist([i, j], SIS) and not_exist([j, i], SIS):
            SI_new.append(SI[j-1])
            SIS.append(j)
            i = j
            j = j + 1
        else:
            j = j + 1
    return SI_new


print(algorithm1_real(SI))
# [1, 2, 3, 4, 5, 1, 3, 5, 2, 4, 1]
print(algorithm1_real(people))
# ['Kenn', 'Tom', 'Jerry', 'Jenifer', 'Candy', 'Kenn', 'Jerry', 'Candy', 'Tom', 'Jenifer', 'Kenn']

import test
import sys
sys.exit(0)