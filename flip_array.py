import numpy as np

a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
a4d = np.array(([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]))
b = np.array(([1, 2, 3], [4, 5, 6]))
print(a)
print(a4d)
print(b)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# [[1 2 3 4]
#  [2 3 4 5]
#  [3 4 5 6]
#  [4 5 6 7]]
# [[1 2 3]
#  [4 5 6]]


def flip180(arr):
    new_arr = arr.reshape(arr.size)
    new_arr = new_arr[::-1]
    new_arr = new_arr.reshape(arr.shape)
    return new_arr


print(flip180(a))
# [[9 8 7]
#  [6 5 4]
#  [3 2 1]]
print(flip180(a4d))
# [[7 6 5 4]
#  [6 5 4 3]
#  [5 4 3 2]
#  [4 3 2 1]]
print(flip180(b))
# [[6 5 4]
#  [3 2 1]]


def flip90_left(arr):
    new_arr = np.transpose(arr)
    new_arr = new_arr[::-1]
    return new_arr


print(flip90_left(a))
# [[3 6 9]
#  [2 5 8]
#  [1 4 7]]
print(flip90_left(a4d))
# [[4 5 6 7]
#  [3 4 5 6]
#  [2 3 4 5]
#  [1 2 3 4]]
print(flip90_left(b))
# [[3 6]
#  [2 5]
#  [1 4]]


def flip90_right(arr):
    new_arr = arr.reshape(arr.size)
    new_arr = new_arr[::-1]
    new_arr = new_arr.reshape(arr.shape)
    new_arr = np.transpose(new_arr)[::-1]
    return new_arr


print(flip90_right(a))
# [[7 4 1]
#  [8 5 2]
#  [9 6 3]]
print(flip90_right(a4d))
# [[4 3 2 1]
#  [5 4 3 2]
#  [6 5 4 3]
#  [7 6 5 4]]
print(flip90_right(b))
# [[4 1]
#  [5 2]
#  [6 3]]

