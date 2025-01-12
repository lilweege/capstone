while True :
    try :
        a = [int(_) for _ in input().split()]
        print(len(str(sum(a))))
    except :
        break