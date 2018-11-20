import numpy as np

# a = [1, 2]
# b = [3, 4]
# c = [5, 6]
#
# t1 = np.append(a, b)
# print(t1)
# # [1 2 3 4]
# t2 = np.append(t1, c)
# print(t2)
# # [1 2 3 4 5 6]
#
# t3 = np.stack((a, b, c))
# print(t3)
# # [[1 2]
# #  [3 4]
# #  [5 6]]
# t4 = np.vstack((a, b, c))
# print(t4)
# # [[1 2]
# #  [3 4]
# #  [5 6]]

# a = 1
# arr = []
# arr = np.append(arr, a)
# print(arr)  # [1.]

a = 'a1'
arr = [a]
arr = np.append(arr, a)
print(arr)  # ['a1' 'a1']
