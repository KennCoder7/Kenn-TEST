import numpy as np

a = np.arange(0, 10)
b = np.arange(0, 15)
c = np.arange(0, 20)
d = np.arange(0, 30)
e = np.arange(10, 40)
f = np.arange(0, 100)


def pick_arange(arange, num):
    if num > len(arange):
        # print("# num out of length, return arange:", end=" ")
        return arange
    else:
        output = np.array([], dtype=arange.dtype)
        seg = len(arange) / num
        for n in range(num):
            if int(seg * (n+1)) >= len(arange):
                output = np.append(output, arange[-1])
            else:
                output = np.append(output, arange[int(seg * n)])
        # print("# return new arange:", end=' ')
        return output


# print(pick_arange(a, 10))
# print(pick_arange(a, 11))
# print(pick_arange(b, 10))
# print(pick_arange(c, 10))
# print(pick_arange(d, 10))
# print(pick_arange(e, 10))
# print(pick_arange(f, 10))
# print(pick_arange(f, 20))

# return new arange: [0 1 2 3 4 5 6 7 8 9]
# num out of length, return arange: [0 1 2 3 4 5 6 7 8 9]
# return new arange: [ 0  1  3  4  6  7  9 10 12 14]
# return new arange: [ 0  2  4  6  8 10 12 14 16 19]
# return new arange: [ 0  3  6  9 12 15 18 21 24 29]
# return new arange: [10 13 16 19 22 25 28 31 34 39]
# return new arange: [ 0 10 20 30 40 50 60 70 80 99]
# return new arange: [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 99]
