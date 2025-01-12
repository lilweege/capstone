# coding: utf-8
# Here your code !

import sys

n = [int(input()) for i in range (1,11)] 
#t = [int(input()) for i in range(n)] 
n.sort()
n.reverse()

for j in range (0,3):
    print(n[j])