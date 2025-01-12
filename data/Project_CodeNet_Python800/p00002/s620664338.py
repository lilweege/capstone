import sys,math
for line in sys.stdin:
    print reduce(lambda x,y: int(math.log10(x+y)+1), map(int, line.split()))