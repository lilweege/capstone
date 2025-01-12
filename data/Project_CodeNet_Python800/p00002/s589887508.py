import math
while True:
    try:
        a,b = [int(x) for x in input().split()]
        x = a + b        
        print(int(math.log10(x))+1)
    except:
        break

