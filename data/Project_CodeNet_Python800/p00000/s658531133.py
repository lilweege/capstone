# coding=utf-8
from __future__ import print_function


def main():
    [print('{:d}x{:d}={:d}'.format(i, j, i * j))
     for i in xrange(1, 10) for j in range(1, 10)]

if __name__ == '__main__':
    main()