#coding: utf-8

import sys

for line in sys.stdin:
    l = map(int,line.split())
    n = l[0] + l[1]
    print len(str(n))