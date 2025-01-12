#!/usr/bin/env python3

import collections
import sys

def read_prob():
    inputs = []
    try:
        while True:
            line = input().strip().split()
            a, b = line[0], line[1]
            inputs.append(int(a) + int(b))
    except EOFError:
        pass
    return inputs

if __name__ == '__main__':
    inputs = read_prob()
    for inp in inputs:
        answer = len(str(inp))
        print(answer)

