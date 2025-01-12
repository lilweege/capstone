import sys
l = []
for i in range(10):
    l.append(int(sys.stdin.readline().rstrip()))
for h in sorted(l,reverse=True)[:3]:
    print(h)