import numpy as np

i = np.arange(10)
np.random.shuffle(i)
print(i)
#
# array = np.array([0, 0])
# for i in range(10):
#     array = np.vstack((array, [i+1, i+1]))
# print(array)
# # [[ 0  0]
# #  [ 1  1]
# #  [ 2  2]
# #  [ 3  3]
# #  [ 4  4]
# #  [ 5  5]
# #  [ 6  6]
# #  [ 7  7]
# #  [ 8  8]
# #  [ 9  9]
# #  [10 10]]
#
# rand_arr = np.arange(array.shape[0])
#
# np.random.shuffle(rand_arr)
# print(array[rand_arr[0:5]])
# # [[9 9]
# #  [4 4]
# #  [1 1]
# #  [5 5]
# #  [8 8]]
# np.random.shuffle(rand_arr)
# print(array[rand_arr[0:5]])
# [[10 10]
#  [ 3  3]
#  [ 4  4]
#  [ 8  8]
#  [ 5  5]]

