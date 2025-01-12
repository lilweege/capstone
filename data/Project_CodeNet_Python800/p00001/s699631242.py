import sys

a = sorted([int(x) for x in sys.stdin.readlines()], reverse=True)
for i in range(3):
    print(a[i])