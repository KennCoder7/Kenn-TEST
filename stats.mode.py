from scipy.stats import mode
import numpy as np

list = ['a', 'a', 'a', 'b', 'b', 'b', 'a']

print("# Print mode(list):", mode(list))
print("# list中最常见的成员为：{}，出现了{}次。".format(mode(list)[0][0], mode(list)[1][0]))
a = np.array([[2, 2, 2, 1],
              [1, 2, 2, 2],
              [1, 1, 3, 3]])
print("# Print mode(a):", mode(a))
print("# Print mode(a.transpose()):", mode(a.transpose()))
print("# a的每一列中最常见的成员为：{}，分别出现了{}次。".format(mode(a)[0][0], mode(a)[1][0]))
print("# a的第一列中最常见的成员为：{}，出现了{}次。".format(mode(a)[0][0][0], mode(a)[1][0][0]))
print("# a的每一行中最常见的成员为：{}，分别出现了{}次。".format(mode(a.transpose())[0][0], mode(a.transpose())[1][0]))
print("# a中最常见的成员为：{}，出现了{}次。".format(mode(a.reshape(-1))[0][0], mode(a.reshape(-1))[1][0]))