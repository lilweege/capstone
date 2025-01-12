import sys
for a in sys.stdin:
    b,c=map(int,a.split())
    d=len(str(b+c))
    print(d)