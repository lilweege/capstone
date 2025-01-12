import math
while True:
	try:
		x,y=map(int,input().split())
		print(int(math.log10(x+y))+1)
	except EOFError:
		break