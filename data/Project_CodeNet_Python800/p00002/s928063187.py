import sys

l = sys.stdin.readlines()
for i in l:
    x,y = map(int,i.split())
    print(len(str(x+y)))