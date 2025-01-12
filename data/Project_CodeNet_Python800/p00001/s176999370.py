a = []
for i in range(10) :
  a.append(int(input()))

a.sort()
a.reverse()
print("%d\n%d\n%d" % (a[0], a[1], a[2]))