from itertools import product
from operator import mul

for v in map(lambda x: (x[0], x[1], mul(*x)), product(range(1, 10), repeat=2)):
    print("{}x{}={}".format(*v))