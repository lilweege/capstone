import sys
for jk in sys.stdin:
    L=jk.split(" ")
    sum = int(L[0])+int(L[1])
    digit = 1
    while sum>=10:
        sum = sum/10
        digit = digit + 1

    print digit