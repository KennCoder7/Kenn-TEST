import numpy as np


def strarr_to_numarr(list):
    list_unique = np.unique(list)
    list_unique_len = len(list_unique)
    new_list = np.array([], dtype=int)
    for i in list:
        for j in range(list_unique_len):
            if list_unique[j] == i:
                new_list = np.append(new_list, int(j))
    return new_list


def numarr_to_strarr(numarr, labels):
    numarr_unique = np.unique(numarr)
    numarr_unique_len = len(numarr_unique)
    if numarr_unique_len != len(np.unique(labels)):
        return print("# Error! Incompatible")
    new_list = np.array([], dtype=str)
    for i in numarr:
        new_list = np.append(new_list, labels[i])
    return new_list


# strarr = ['cat', 'dog', 'cat', 'fish']
# numarr = strarr_to_numarr(strarr)
# print(numarr)
# print(numarr_to_strarr(numarr, strarr))
# [0 1 0 2]
# ['cat' 'dog' 'cat' 'cat']

y_true = np.array(['cat', 'dog', 'pig', 'cat', 'dog', 'pig'])
print(strarr_to_numarr(y_true))
print(numarr_to_strarr(strarr_to_numarr(y_true), ['cat', 'dog', 'pig']))
print(numarr_to_strarr(strarr_to_numarr(y_true), ['cat', 'dog', 'pig']) == y_true)