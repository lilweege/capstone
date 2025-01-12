import sys

for i in sys.stdin:
    num = map(int, i.split())
    print len(str(sum(num)))