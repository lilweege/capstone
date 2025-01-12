import sys

while True:
    try:
	a,b = raw_input().split()
	c = int(a) + int(b)
	for i in range(10):
	    if c / (10**i) == 0:
		print (i)
		break
    except EOFError:
	break