import sys

for line in sys.stdin:
	l = map(int, line.split())
	print len(str(l[0]+l[1]))