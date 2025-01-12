import sys
import math

for line in sys.stdin:
  a = line.split()
  print int(math.log10(int(a[0]) + int(a[1]))) + 1