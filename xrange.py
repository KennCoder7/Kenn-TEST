from six.moves import xrange

for i in xrange(1, 6):
    print(i)

for i in range(1, 6):
    print(i)

print(xrange(1, 6) == range(1, 6))  # True