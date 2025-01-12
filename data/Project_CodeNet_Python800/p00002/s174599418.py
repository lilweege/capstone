import sys
from operator import add
from math import log10

for i in sys.stdin:
    print(int(log10(add(*list(map(int, i.split()))))) + 1)