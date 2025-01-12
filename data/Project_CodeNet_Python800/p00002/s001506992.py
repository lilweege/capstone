import sys
for i in sys.stdin.readlines():
    a,b = map(int,i.split())
    print len(str(a+b))