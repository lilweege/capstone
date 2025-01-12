x = []

for i in xrange(10):
    x.append(input())

x.sort()
x = x[::-1]
for i in xrange(3):
    print x[i]