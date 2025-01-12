N = int(input())
for i in range(N):
    triangle = sorted([int(n) for n in input().split()])
    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print('YES')
    else:
        print('NO')

