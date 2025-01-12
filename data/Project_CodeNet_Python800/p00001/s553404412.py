import sys

data = []

for d in sys.stdin:
  data.append(int(d))

data.sort(reverse=True)
for i in xrange(3):
  print data[i]