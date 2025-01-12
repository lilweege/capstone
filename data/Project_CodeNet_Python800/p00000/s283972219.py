from itertools import product
for i, j in product(range(1, 10), repeat=2):
    print('{}x{}={}'.format(i, j, i * j))