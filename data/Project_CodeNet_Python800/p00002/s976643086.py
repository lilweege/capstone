#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    try:
        a, b = map(int , input().split())
        sum = a + b
        print(len(str(a + b)))
    except:
        break