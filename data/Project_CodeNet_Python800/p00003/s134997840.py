# -*- coding: utf-8 -*-

import sys

def is_right_triangle(hypotenuse, x, y):
    if x**2 + y**2 == hypotenuse**2:
        return True
    return False

def main():
    N = int(input())
    for i in range(N):
        length = [int(n) for n in input().split()]
        length.sort(reverse=True)
        ret = 'YES' if is_right_triangle(*length) else 'NO'
        print(ret)

if __name__ == '__main__':
    main()