while True:
    try:
        x,y=[int(i) for i in input().split()]
        print(len(str(x+y)))
    except:
        break;