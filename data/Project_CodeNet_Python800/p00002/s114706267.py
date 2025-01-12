import math
while True:
        try:
                a =map(int,raw_input().split())
                b = a[0] + a[1]
                print len(str(a[0]+a[1]))
        except EOFError:
                break