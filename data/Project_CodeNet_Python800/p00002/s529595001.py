# coding=utf-8
import math


while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    c = a + b
    digit = int(math.log10(c) + 1)
    print(digit)