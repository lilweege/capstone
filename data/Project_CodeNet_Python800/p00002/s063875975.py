#xs = [int(x) for x in input().split()]
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    i = a + b
    j = 1
    while i >= 10:
        i = i / 10
        j = j + 1
    print(j)