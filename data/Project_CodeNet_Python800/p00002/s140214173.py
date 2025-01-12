results=[]
from sys import stdin
for line in stdin:
    a, b = (int(i) for i in line.split())
    results.append(len(str(a+b)))
for i in results:
    print i