while True:
    try:
        a,b = map(int,input().split())
    except:
        exit()

    print(len(str(a+b)))