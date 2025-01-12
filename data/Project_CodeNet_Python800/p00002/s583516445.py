import math
import sys
for line in sys.stdin:
    a,b = map(int, line.split())
    print(int(math.log10(a+b) + 1))