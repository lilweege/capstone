
# coding: utf-8
# Here your code !

import sys
import math

list = ["2","3"]
r = sys.stdin.readlines()

n = [[int(i) for i in (j.split())] for j in r]
#e = [[int(i) for i in input().split()] for i in range(n)] 

for j in n:
    a = sum(j)
    d = int(math.log10(a)) + 1
    print(d)