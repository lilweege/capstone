while 1:
    try:
        x,y=input().split()
        k=int(x)+int(y)
        print(len(str(k)))
    except EOFError:
        break