while 1:
    try:
        a,b = input().split()
        a = int(a)
        b = int(b)
        c = a + b
        print(len(str(c)))
    except EOFError:
        break
