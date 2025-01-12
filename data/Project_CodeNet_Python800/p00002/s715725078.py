import sys

for line in sys.stdin:
    sum = 0
    for x in line.split():
        sum += int(x)
    print(len(str(sum)))