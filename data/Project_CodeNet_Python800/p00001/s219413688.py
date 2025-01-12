# coding: utf-8

list = []

for i in range(10):
    list.append(int(input()))

slist = sorted(list)

for i in range(3):
    print(slist[9-i])