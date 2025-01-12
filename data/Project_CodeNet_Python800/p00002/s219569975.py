import math
import sys

for num in sys.stdin:
	num = num.split()
	a = int(num[0])
	b = int(num[1])
	size = int (math.log10(a+b) + 1)
	print(size)
