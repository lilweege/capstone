#condig: UTF-8

while True:
    try:
        n = map(int, raw_input().split())
        s = len(str(n[0] + n[1]))
        print s
    except Exception:
        break