import sys
for l in sys.stdin:
	print len(str(sum(map(int,l.split()))))