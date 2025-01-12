import sys
import math

for i in sys.stdin.readlines():
    a, b = map(int, i.strip().split())
    print "{}".format(int(math.log10(a+b))+1)