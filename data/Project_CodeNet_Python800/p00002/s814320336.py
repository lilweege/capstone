import sys
import math

for x in sys.stdin.readlines():
	a, b = map(int, x.strip().split())
	print int(math.log10(a + b)) + 1