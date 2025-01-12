from math import log10 as log
from sys import stdin
A = []
for po in stdin:
    S = list(map(int,po.split()))
    A.append(int(log(S[0]+S[1])+1))
for i in A:
    print(i)