while True:
    try:
        x = map(int, raw_input().split(" "))
        print len(str(x[0]+x[1]))

    except EOFError:
        break