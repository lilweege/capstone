while True:
    try:
        a, b = map(int, input().rstrip().split())
        print(len(str(a + b)))
    except Exception:
        break
