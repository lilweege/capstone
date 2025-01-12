import sys
for n in [sum([int(m) for m in l.split()]) for l in sys.stdin]:
	print len(str(n))