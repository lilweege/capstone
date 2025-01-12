#coding: utf-8

temp = []
for i in range(10):
    N = input()
    temp.append(N)
temp.sort()
print temp[-1]
print temp[-2]
print temp[-3]