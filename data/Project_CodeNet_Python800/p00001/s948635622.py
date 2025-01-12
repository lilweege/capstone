#coding:utf-8

l = []
for i in xrange(10):
    a = input()
    l.append(a)

for n in xrange(3):
    print(max(l))
    l.remove(max(l))