#coding UTF-8

n = []
for i in range(10):
    n.append(input())
n.sort()
n.reverse()
for i in range(3):
    print n[i]