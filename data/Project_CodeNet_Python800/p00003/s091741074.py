n = int(input())

for i in range(n):
    a,b,c = list(map(int, input().split()))
    M = max([a,b,c])
    result = False
    if a == M:
        result = (a * a == b * b + c * c)
    elif b == M:
        result = (b * b == a * a + c * c)
    elif c == M:
        result = (c * c == a * a + b * b)
    if result:
        print("YES")
    else:
        print("NO")