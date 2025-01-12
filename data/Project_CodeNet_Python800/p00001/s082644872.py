from sys import stdin

for x in sorted([int(l) for l in stdin],reverse=True)[0:3]:
  print(x)