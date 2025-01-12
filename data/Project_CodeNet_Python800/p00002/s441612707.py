while True:
    try:
        
        a = map(int,raw_input().split(' '))
        s = a[0] + a[1]
        c = 0
        while s > 0:
            s = s / 10
            c = c + 1
            if s <= 0:
                print c
                break
                
    except (EOFError):
        break