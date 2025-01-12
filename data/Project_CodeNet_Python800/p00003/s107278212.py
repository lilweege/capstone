ans = []
for i in range(int(input())):
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    lst.sort()
    if lst[2]**2 == lst[0]**2 + lst[1]**2:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)