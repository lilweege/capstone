while True:
    try:
        a, b = map(int, input().split())
        i = a + b
        c = 1
        while i:
            if int(i/10) == 0:
                print(c)
                break
            c+=1
            i /= 10
    except Exception:
        break