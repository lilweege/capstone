#!/usr/bin/env python
# -*- coding: utf-8 -*-

m = []
for i in range(0,10):
    m.append(int(input()))

for i in range(0,3):
    print(list(reversed(sorted(m)))[i])