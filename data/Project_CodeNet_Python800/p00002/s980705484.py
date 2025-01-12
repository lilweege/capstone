# coding: utf-8
import sys

N = sys.stdin.read().splitlines()

for n in N:
    i, j = [int(i) for i in n.split()]
    print(len(str(i+j)))