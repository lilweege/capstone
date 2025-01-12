# -*- coding: utf-8 -*-

import sys

def top_k_sort(data, k=3, reverse=True):
    data.sort(reverse=True)
    return data[:k]

def main():
    data = []
    for line in sys.stdin:
        data.append(int(line))

    for h in top_k_sort(data):
        print(h)

if __name__ == '__main__':
    main()