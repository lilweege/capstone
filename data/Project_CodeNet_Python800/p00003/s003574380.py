import sys

n = input()

for _ in range(int(n)):
  a, b, c = sorted(map(int, sys.stdin.readline().split()))
  if a * a + b*b == c* c:
    print("YES")
  else:
    print("NO")