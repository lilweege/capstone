while True:
    try:
        a,b = map(int, input().split())
        d = 0
        s = sum([a,b])
        while (s):
            s //= 10
            d += 1
        print(d)
    except EOFError: break
    
