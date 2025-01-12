import sys

a = []
for i in sys.stdin:
    a.append(int(i.replace("\n", "")))
a.sort(reverse=True)
del a[3:]
print( "\n".join(map(str, a)))