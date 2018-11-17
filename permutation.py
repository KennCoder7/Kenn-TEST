import numpy as np
import itertools as it


# def permu_array(arr):
#     re_array_method = np.array(list(it.permutations([1, 2, 3])))
#     out_array = arr
#     new_array = np.array([], dtype=float)
#     for n in range(re_array_method.shape[0]):
#         for i in range(len(arr)):
#             if n != 0:
#                 new_array = np.append(new_array, arr[re_array_method[n][i] - 1])
#     out_array = np.append(out_array, new_array)
#     return out_array  # [1. 2. 3. 1. 3. 2. 2. 1. 3. 2. 3. 1. 3. 1. 2. 3. 2. 1.]
#
#
# print(permu_array([1, 2, 3]))  # [1. 2. 3. 1. 3. 2. 2. 1. 3. 2. 3. 1. 3. 1. 2. 3. 2. 1.]


def array_algorithm1(arr):
    re_array_method1 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8], dtype=int)
    re_array_method2 = np.array([1, 4, 7, 1, 5, 8, 2, 5, 9], dtype=int)
    re_array_method3 = np.array([3, 6, 9, 4, 8, 3, 7, 2, 6], dtype=int)
    # new_array = np.array([], dtype=float)
    new_array1 = np.array([], dtype=float)
    new_array2 = np.array([], dtype=float)
    new_array3 = np.array([], dtype=float)
    for i in range(len(arr)):
        new_array1 = np.append(new_array1, arr[re_array_method1[i] - 1])
        new_array2 = np.append(new_array2, arr[re_array_method2[i] - 1])
        new_array3 = np.append(new_array3, arr[re_array_method3[i] - 1])
    new_array = np.append(arr, new_array1)
    new_array = np.append(new_array, new_array2)
    new_array = np.append(new_array, new_array3)
    return new_array  # 123456789 135792468 147158259 369483726


def array_algorithm2(arr):
    re_array_method = np.array([[1, 3, 5, 7, 9, 2, 4, 6, 8], [1, 4, 7, 1, 5, 8, 2, 5, 9], [3, 6, 9, 4, 8, 3, 7, 2, 6]],
                               dtype=int)
    new_array = np.array([], dtype=float)
    for n in range(re_array_method.shape[0]):
        for i in range(len(arr)):
            new_array = np.append(new_array, arr[re_array_method[n][i] - 1])
    out_array = np.append(arr, new_array)
    return out_array  # 123456789 135792468 147158259 369483726


print(array_algorithm1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(array_algorithm2([1, 2, 3, 4, 5, 6, 7, 8, 9]))


