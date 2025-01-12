import sys
for line in sys.stdin.readlines():
    a,b = map(int, line.strip().split())
    print len(str(a+b))