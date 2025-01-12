while 1:
    try:
        a, b = map(int, input().split())
        ans = 1
        while (a+b)/(10**ans) >= 1:
            ans += 1
        print(str(ans))
    except EOFError:
        break
