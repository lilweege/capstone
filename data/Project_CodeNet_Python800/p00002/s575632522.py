# coding: utf-8
import sys
import math

numbers = []
for line in sys.stdin:
    numbers.append(line.split())

for i in range(len(numbers)):
    sum = int(numbers[i][0]) + int(numbers[i][1])
    print int(math.log10(float(sum))) + 1