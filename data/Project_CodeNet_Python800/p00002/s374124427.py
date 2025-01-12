import sys

for i in sys.stdin:
  a, b = map(int, i.split())
  print len(str(a+b))