import sys
a = []
b = []

for i in sys.stdin:
    ta, tb = i.split()
    a.append(int(ta))
    b.append(int(tb))

for i in range(len(a)):
    print len(str(a[i]+b[i]))