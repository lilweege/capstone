n=int(input())
for _ in range(n):
    a=sorted([int(i) for i in input().split()])
    print("YES" if a[0]**2+a[1]**2==a[2]**2 else "NO")