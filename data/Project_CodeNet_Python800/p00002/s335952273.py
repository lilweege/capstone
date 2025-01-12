while True:
    try:
        print len(list(str(sum(map(int,raw_input().split())))))
    except: 
        break