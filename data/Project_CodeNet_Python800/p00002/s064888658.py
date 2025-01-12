import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    x = a+b
    c = 0
    while x/10 > 0:
        x /= 10        
        c += 1
    print c+1