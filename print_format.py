# a = 1
# b = 2
# print('a=%d, b=%d' % (a, b))

# print ("His name is %s" % "Kenn")

# print ("He is %d years old" % 25)
# print("He is %d years old, and born in %d" % (25, 1990))
# print("His height is %f m" % 1.83)

# print("His height is %.2f m" % 1.84)
# print("His height is %.1f m" % 1.84)
# print("His height is %.2f m" % 1.85)
# print("His height is %.1f m" % 1.85)

print("Name:%10s Age:%8d Height:%8.2f" % ("Kenn", 25, 1.83))
print("\n")
print("Name:%-10s Age:%-8d Height:%-8.2f" % ("Kenn", 25, 1.83))
print("\n")
print("Name:%-10s Age:%08d Height:%08.2f" % ("Kenn", 25, 1.83))

# print(format(0.00154, '.2e'))
# print(format(154000, '.2e'))
# print(format(0.00154, '.1e'))
# print(format(154000, '.1e'))
# print(format(0.00155, '.1e'))
# print(format(155000, '.1e'))