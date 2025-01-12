while True:
    try:
        line = input()
    except:
        break
    a, b = map(int, line.strip().split())
    print(len(str(a + b)))