# -*- coding: utf-8 -*-

a = [int(raw_input()) for _ in range(10)]
#print a
b = sorted(a, reverse=True)
#print b
for c in b[0:3]:
    print c