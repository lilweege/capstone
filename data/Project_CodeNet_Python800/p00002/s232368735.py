try:
    s = []
    while True:
        l = input().split()
        t = int(l[0]) + int(l[1])
        n = str(t)
        print(len(n))
except EOFError:
    pass