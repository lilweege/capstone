import math
while True:
    try:
        lst = list(map(int, input().split()))
        a, b = lst[0], lst[1]
        c = str(a+b)
        print(len(c))

    except EOFError:
        break
