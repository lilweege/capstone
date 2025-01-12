from itertools import product

for i, j in product(range(1,10), repeat=2):
    print('%dx%d=%d' % (i, j, i*j))