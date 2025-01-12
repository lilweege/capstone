import sys
for line in sys.stdin:
	l = map(lambda i:int(i), line.split(' '))
	print len(str(l[0] + l[1]))