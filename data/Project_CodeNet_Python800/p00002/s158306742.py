from sys import stdin
import math
import fileinput

for line in fileinput.input():
    a, b = [int(n) for n in line.split()]
    print(math.floor(math.log10(a + b) + 1))
    # x1, y1, x2, y2, x3, y3, xp, yp = [float(r) for r in line]
    # print(x1, y1, x2, y2, x3, y3, xp, yp)