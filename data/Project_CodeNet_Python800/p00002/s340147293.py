import sys, math

for line in sys.stdin:
    print int(math.log10(sum(map(int, line.split())))) + 1