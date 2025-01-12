import sys

l = sorted(map(int,sys.stdin.readlines()),reverse=True)
for i in l[:3]:
    print(i)