import sys
values = []
for line in sys.stdin:
    values.append([int(x) for x in line.split()])
digit = 0
for x, y in values:
    sum = x + y; digit = 0
    while sum >= 1:
        sum //= 10
        digit += 1
    print(digit)