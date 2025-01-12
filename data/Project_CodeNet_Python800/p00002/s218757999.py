import math

lst = []
while True:
    try:
        a, b = map(int, input().split())
        lst.append(int(math.log10(a+b))+1)
    except EOFError:
        for i in lst:
            print(i)
        break