while True:
    try:
        a=map(int,raw_input().split())
        print len(str(a[0]+a[1]))
    except:
        break