N=int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a):
        print('YES')
    else:
        print('NO')