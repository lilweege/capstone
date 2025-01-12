import sys
from math import log10, floor
print('\n'.join(map(str, [floor(log10(sum(map(int, ab.split())))) + 1 for ab in sys.stdin])))