import sys

data = sys.stdin.readline()
l = list()
while data:
    l.append(int(data))
    data = sys.stdin.readline()

for x in sorted(l,reverse=True)[:3]:
    print(x)