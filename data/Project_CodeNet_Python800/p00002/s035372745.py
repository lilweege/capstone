import sys
for e in sys.stdin:print(len(str(sum(map(int,e.split())))))
