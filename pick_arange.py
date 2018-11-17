import numpy as np

a = np.arange(0, 10)
# print(a)    # [0 1 2 3 4 5 6 7 8 9]
b = np.arange(0, 15)
# print(b)    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
c = np.arange(0, 20)
# print(c)    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]


def pick_arange(arange, num):
    if num > len(arange):
        print("# Error pick!")
    else:
        output = []
        seg = round((len(arange)) / num, 2)
        for n in range(num):
            output = np.append(output, arange[int(seg*n)])
        return output


print(pick_arange(a, 10))
print(pick_arange(b, 10))
print(pick_arange(c, 10))
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
# [ 0.  1.  3.  4.  6.  7.  9. 10. 12. 13.]
# [ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18.]
