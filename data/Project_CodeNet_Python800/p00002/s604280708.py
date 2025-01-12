import sys
for s in sys.stdin:
    x=len(str(sum(map(int,s.split())))) 
    print x