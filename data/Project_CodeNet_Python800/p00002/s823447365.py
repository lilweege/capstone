while(True):
    try:
        a = map(int, raw_input().split())
        b = str(a[0] + a[1])
        print(len(b))
    except Exception:
        break