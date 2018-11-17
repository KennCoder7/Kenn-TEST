n = input("1st enter:")
print(n)
print(type(n))

n = int(input("2nd enter:"))
print(n)
print(type(n))

n, m, c = input("3rd enter:")
print(n, m, c)
print(type(n))

n, m, c = eval(input("3rd enter:"))
print(n, m, c)
print(type(n))


# 1st enter:1
# 1
# <class 'str'>
# 2nd enter:1
# 1
# <class 'int'>
# 3rd enter:123
# 1 2 3
# <class 'str'>
# 4th enter:1,2,3
# 1 2 3
# <class 'int'>