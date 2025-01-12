import math
import sys

while True:
	try:
		a,b = map(int, input().split())
		print(len(str(a+b)))
	except EOFError:
		break