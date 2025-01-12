import sys
for line in sys.stdin.readlines():
    a, b = map(int,line.split())
    c=int(a+b)
    count=0
    while (c/10 != 0 ):
        c=int(c/10)
        count=count+1
    print(count)