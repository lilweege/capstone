from math import log10
while True:
	try:
		a, b = map(int, raw_input().split())
		print(int(log10(a+b)) + 1)
	except EOFError:
		break