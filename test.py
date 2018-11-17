import numpy as np
import itertools as it

# print(np.array(([], []), dtype=int).shape)  # (2, 0)
# print(np.array(([[], []], [[], []]), dtype=int).shape)  # (2, 2, 0)
test = [1, 2, 3]
test0 = it.permutations(test, 3)
print("print test0: ", test0)
# print test0:  <itertools.permutations object at 0x000001B87F78FC50>
test1 = list(test0)
print("print test1: ", test1)
# print test1:  [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
test2 = np.array(test1)
print("print test2: ", test2.shape, test2)
# print test2:  (6, 3) [[1 2 3]
#  [1 3 2]
#  [2 1 3]
#  [2 3 1]
#  [3 1 2]
#  [3 2 1]]
test3 = list(test2)
print("print test3: ", test3)
# print test3:  [array([1, 2, 3]), array([1, 3, 2]), array([2, 1, 3]),
# array([2, 3, 1]), array([3, 1, 2]), array([3, 2, 1])]
test4 = np.split(test2, 6)
print("print test4: ", test4)
# print test4:  print test4:  [array([[1, 2, 3]]), array([[1, 3, 2]]), array([[2, 1, 3]]),
# array([[2, 3, 1]]), array([[3, 1, 2]]), array([[3, 2, 1]])]

