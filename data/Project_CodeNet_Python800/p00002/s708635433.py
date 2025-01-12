try:
    while True:
        a,b=map(int, input().split())
        print(len(str(a+b)))
except EOFError:
    pass