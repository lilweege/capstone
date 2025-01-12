N = int(input())
for i in range(N):
    a,b,c = map(int,input().split())
    if a*a + b*b == c*c or b*b+c*c == a*a or a*a+c*c == b*b:
        print("YES")
    else:
        print("NO")