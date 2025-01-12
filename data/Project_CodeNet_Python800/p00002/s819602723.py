while True:
    try:
        x = input()
        a, b = list(map(int, x.split()))
        c = a + b
        print(len(str(c)))
    except:
        break