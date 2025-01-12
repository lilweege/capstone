try:
    while True:
        a, b = [int(x) for x in input().strip().split(' ')]
        print(len(list(str(a+b))))
except EOFError:
    pass
