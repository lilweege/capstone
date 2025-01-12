import math

while True:
	try:
		a, b = map(int, input().split())
		print(int(math.log10(a + b)) + 1)
	except EOFError:
		break