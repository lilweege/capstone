# -*- coding:utf8 -*-
import sys
import math
for s in sys.stdin:
    a,b = map(int, s.split(' '))
    print int(math.log10(a+b)) + 1