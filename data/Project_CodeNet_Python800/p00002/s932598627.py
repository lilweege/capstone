while 1:
    try:
        i = list(map(int, input().split()))
        print(len(str(i[0]+i[1])))
    except:
        break