# -*- coding: utf-8 -*-

temp = 0
for i in range(1,10):
    for k in range(1,10):
        temp = i * k
        print("%dx%d=%d" % (i, k, temp))