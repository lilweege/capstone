from sys import stdin
for l in stdin:
  a,b=map(int,l.split())
  print(len(str(a+b)))