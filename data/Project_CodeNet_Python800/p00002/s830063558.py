#!/usr/bin/env python3
#coding: utf-8

# Volume0 - 0002 (http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002)

while 1:
    try:
        i = input()
        l = i.split(" ")
        s = int(l[0]) + int(l[1])
        ans = len(str(s))
        print(ans)
    except:
        break