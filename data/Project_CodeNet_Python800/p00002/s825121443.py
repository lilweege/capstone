import sys
for jk in sys.stdin:
    j,k=map(int,jk.split())
    print len(str(j+k))