#!/usr/bin/env python3
#coding: utf-8

# Volume0 - 0001 (http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0001)

li = []
for x in range(10):
    s = input()
    s = int(s)
    li.append(s)

li.sort()
li.reverse()

for y in range(3):
    print(li[y])