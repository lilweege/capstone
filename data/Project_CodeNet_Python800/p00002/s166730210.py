while True:
    try:
        s = input()
        a, b = [int(i) for i in s.split()]
        print(len(str(a + b)))
    except:
        break

