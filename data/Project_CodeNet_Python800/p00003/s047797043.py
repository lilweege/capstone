# -*- coding:utf-8 -*-

import sys

array = []
for i in sys.stdin:
    array.append(i)

N = int(array[0])
for k in range(1,N+1):
    x = array[k].split()
    a, b, c = int(x[0]), int(x[1]), int(x[2])
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print('YES')
    else:
        print('NO')