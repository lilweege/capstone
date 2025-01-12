import sys

d = sys.stdin.readline()
while d:
    a, b = map(int,d.split())
    print(len(str(a+b)))
    d = sys.stdin.readline()