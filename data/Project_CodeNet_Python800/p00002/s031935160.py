# -*- coding: utf-8 -*-

import sys

def get_digits(n):
    if n < 0:
        n *= -1
    return len(str(n))


def main():
    data = []
    for line in sys.stdin:
        a, b = map(int, line.split())
        digits = get_digits(a+b)
        print(digits)

if __name__ == '__main__':
    main()