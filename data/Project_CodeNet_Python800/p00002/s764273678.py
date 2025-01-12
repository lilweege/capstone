import sys

su = 0
for line in sys.stdin:
    for x in line.split():
        su += int(x)
    su = str(su)
    size = len(su)
    print(size)
    su = 0