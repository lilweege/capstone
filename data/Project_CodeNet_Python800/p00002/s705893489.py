while 1:
    try:
        a,b = map(int, raw_input().split())
        n = a+b
        print len(str(n))
    except EOFError:
        break