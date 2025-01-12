import itertools

for x, y in itertools.product(range(1, 10), range(1, 10)):
    print("%dx%d=%d" % (x, y, x * y))