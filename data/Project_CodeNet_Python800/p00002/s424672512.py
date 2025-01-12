import sys

while (True):
    L = map(int, sys.stdin.readline().split())

    if L:
        (a, b) = L
        c = a + b
    
        cnt = 1
        while (c >= 10):
            c /= 10
            cnt += 1

        print cnt

    else:
        break