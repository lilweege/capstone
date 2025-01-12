N=int(input())
for i in range(N):
    lst=sorted([int(s) for s in input().split()],reverse=True)
    if lst[0]**2 == lst[1]**2+lst[2]**2:
        print("YES")
    else:
        print("NO")