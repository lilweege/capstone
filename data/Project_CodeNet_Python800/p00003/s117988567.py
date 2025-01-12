N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    if(a > c):
        a, c = c, a
    if(b > c):
        b, c = c, b
    if(c**2 == a**2 + b**2):
        print("YES")
    else:
        print("NO")