import sys

def log10(num):
    log = 0
    while num > 0:
        log += 1
        num //= 10
    return log

for line in sys.stdin:
    a, b = map(int, line.split())
    print(log10(a + b) if a + b else 1)