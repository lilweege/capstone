import sys

for line in sys.stdin:
    l = line.replace('\n', '')
    a, b = l.split()
    a = int(a)
    b = int(b)
    print(len(str(a+b)))