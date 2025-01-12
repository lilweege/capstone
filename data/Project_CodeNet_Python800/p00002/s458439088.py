# -*- coding: utf-8 -*-

import sys
import os

for s in sys.stdin:
    a, b = list(map(int, s.split()))
    c = a + b

    if c == 1:
        print(1)
        continue

    for i in range(7):
        left = 10 ** i
        right = 10 ** (i + 1)
        if left <= c < right:
            print(i + 1)
            break