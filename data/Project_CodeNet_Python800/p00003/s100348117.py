count=int(input())
for i in range(0, count):
    a = map(int, input().split(' '))
    a = [j**2 for j in a]
    a.sort()
    if (a[0] + a[1] == a[2]):
        print('YES')
    else:
        print('NO')