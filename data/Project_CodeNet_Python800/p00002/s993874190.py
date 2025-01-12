import sys
for x in sys.stdin:
	s = x.split()
	a,b = int(s[0]), int(s[1])
	print(len(str(a+b)))
