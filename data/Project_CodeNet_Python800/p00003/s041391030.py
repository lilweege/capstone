for _ in range(int(input())):
    x = list(sorted(map(int, input().split())))
    print("YES" if x[0]**2 + x[1]**2 == x[2]**2 else "NO")