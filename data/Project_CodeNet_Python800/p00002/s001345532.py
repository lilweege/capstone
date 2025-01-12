# -*- coding:utf-8 -*-
import sys
import math

array =[]
for line in sys.stdin:
    array.append(line)
    
for i in range(len(array)):
    num = array[i].split(' ')
    a = int(num[0])
    b = int(num[1])
    n = a + b
    print(int(math.log10(n) + 1))