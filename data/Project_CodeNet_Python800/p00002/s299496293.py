import sys

d = sys.stdin.readlines()
for i in d:
    a, b = [int(x) for x in i.split()]
    print(len(str(a + b)))