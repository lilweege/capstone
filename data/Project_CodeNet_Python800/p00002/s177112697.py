#!/usr/bin/env python3
import math
import sys

for line in sys.stdin:
    [a, b] = [int(x) for x in line.split()]
    print(int(math.log10(a + b) + 1))