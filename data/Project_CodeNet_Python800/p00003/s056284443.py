n = int(input())
for _ in range(n):
    edges = sorted([int(i) for i in input().split()])
    if edges[0] ** 2 + edges[1] ** 2 == edges[2] ** 2:
        print("YES")
    else:
        print("NO")

