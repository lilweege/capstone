for var in range(1,2001):
    try:
        a,b=map(int,input().split())
        c=a+b
        c=str(c)
        print(len(c))
    except:
        break