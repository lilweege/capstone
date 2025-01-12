import sys
for e in sys.stdin.readlines():
 print(len(str(sum(map(int,e.split())))))
