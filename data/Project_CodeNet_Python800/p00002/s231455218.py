import sys
for l in sys.stdin:
    n, m = map(int, l.split())
    print(len(str(n+m)))