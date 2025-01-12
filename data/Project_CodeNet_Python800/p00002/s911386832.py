import sys

for line in iter(sys.stdin.readline, ""):
  sp = line.rstrip().split(" ")
  sum = int(sp[0])+int(sp[1])
  print len(str(sum))