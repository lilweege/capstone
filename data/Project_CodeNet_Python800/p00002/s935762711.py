import math
while 1:
    try:
        print(int(math.log10(sum(map(int, input().split())))+1))
    except:
        break