import sys

a = []
for line in sys.stdin:
    a.append(int(line))
a.sort()
a.reverse()
print(a[0])
print(a[1])
print(a[2])