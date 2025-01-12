import sys

for line in sys.stdin:
    a,b = [int(i) for i in line.split()]
    print(len(str(a+b)))
