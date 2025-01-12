# -*- coding: utf-8 -*-

import sys

for line in sys.stdin.readlines():
    a, b = map(int, line.strip().split())
    n = a + b
    ans = 1
    while(n >= 10):
        n /= 10
        ans += 1
    print ans