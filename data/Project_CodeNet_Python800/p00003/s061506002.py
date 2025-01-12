N = int(input())
while N > 0:
    es = sorted(list(map(int, input().split())))
    if es[2] ** 2 == es[1] ** 2 + es[0] ** 2:
        print('YES')
    else:
        print('NO')
    N -= 1