while 1:
    try:
        a,b=map(int,input().split())
        print(len(str(a+b)))
    except:
        break