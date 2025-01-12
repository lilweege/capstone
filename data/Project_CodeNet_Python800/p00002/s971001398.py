import sys

for s in sys.stdin:
  a,b = s.split(' ')
  c = int(a) + int(b)
  i = 1

  while c >= 10:
    c = c / 10
    i = i + 1

  print i