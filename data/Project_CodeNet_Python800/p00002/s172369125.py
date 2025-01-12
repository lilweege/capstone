while True:
    try:
        x = list(map(int, input().split(' ')))
        n = x[0] + x[1]
        print(len(str(n)))
    except EOFError:
        break