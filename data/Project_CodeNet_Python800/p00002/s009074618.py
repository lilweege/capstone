import sys
import math

for line in sys.stdin:
  try:
    a, b = [int(i) for i in line.split()]
    print(int(math.log10(a + b) + 1))
  except:
    break