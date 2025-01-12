import sys
import math

for line in sys.stdin:
    l = line.split()
    digit = int(math.log10(int(l[0]) + int(l[1]))) + 1
    print(digit)