import sys
for line in sys.stdin:
    ns = list(map(int, line.split()))
    print(len(str(sum(ns))))