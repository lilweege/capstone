from sys import stdin
ns = [int(n) for n in stdin]
ns.sort(reverse = True)
for i in range(3):
  print(ns[i])