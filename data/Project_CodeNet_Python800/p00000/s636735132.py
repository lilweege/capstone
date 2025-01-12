#!/usr/bin/env python
# -*- coding: utf-8 -*-

for x in range(1, 10):
    for y in range(1, 10):
        s = '%dx%d=%d' % (x, y, x*y)
        print(s)