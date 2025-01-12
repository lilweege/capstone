import sys
for s in sys.stdin:print len(str(sum(map(int,s.split()))))