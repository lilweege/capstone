import sys

for line in sys.stdin:
	a, b = map(int, line.split())
	digitNumber = len(str(a + b))
	print(digitNumber)