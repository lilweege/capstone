deta_set_count = int(input())
for _ in range(deta_set_count):
    k = list(map(int, input().split()))
    k= sorted(k)
    if k[0]**2 + k[1]**2 == k[2]**2:
        print('YES')
    else:
        print('NO')