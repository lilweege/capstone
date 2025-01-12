
while 1:
    try:
        a, b = map(int, input().split())
        c = str(a + b)

        print(len(c))
    except:
        break