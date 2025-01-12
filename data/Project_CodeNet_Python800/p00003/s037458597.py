# Aizu Problem 0003: Is it a Right Triangle?
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


N = int(input())
for __ in range(N):
    a, b, c = sorted([int(_) for _ in input().split()])
    print("YES" if c**2 == a**2 + b**2 else "NO")