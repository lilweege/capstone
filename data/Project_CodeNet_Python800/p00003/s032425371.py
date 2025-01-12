n = int(raw_input())

while n > 0:
  d = map(int, raw_input().split())
  d.sort()
  a = d[0]
  b = d[1]
  c = d[2]

  if (c*c) == (a*a + b*b):
    print "YES"
  else:
    print "NO"

  n = n-1