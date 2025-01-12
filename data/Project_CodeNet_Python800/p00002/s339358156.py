import sys

for line in sys.stdin:
    result = 0
    a, b = map(int, line.rstrip('\n').split(' '))
    x = a + b
    while x  > 0:
        result += 1
        x /= 10
    print result