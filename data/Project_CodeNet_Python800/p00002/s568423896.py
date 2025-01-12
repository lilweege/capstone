import math
while True:
	try:
		a,b=map(int, raw_input().split())
		print int(math.log10(a+b) + 1)
	except:
		break