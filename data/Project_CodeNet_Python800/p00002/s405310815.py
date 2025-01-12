while True:
    try:
        a,b = map(int,raw_input().split())
        c=str(a+b)
        print len(c)
    except EOFError:
        break