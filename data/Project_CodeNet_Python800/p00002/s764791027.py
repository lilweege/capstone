# coding: utf-8
import sys
import math

for line in sys.stdin:
    l = map(int, line.split())
    print len(str(sum(l)))