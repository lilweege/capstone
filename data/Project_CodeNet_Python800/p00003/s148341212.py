N = int(input())
lst = []
for _ in range(N):
    a, b, c = map(int,input().split())
    lst.append([a, b, c])
for i in lst:
    i.sort()
    if i[0] ** 2 + i[1] ** 2 == i[2] ** 2:
        print('YES')
    else:
        print('NO')
    

