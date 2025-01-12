import sys
n = int(input())
for i in range(n):
    ns = [x * x for x in map(int, input().split())]
    if ns[0] + ns[1] == ns[2] or ns[0] + ns[2] == ns[1] or ns[1] + ns[2] == ns[0]:
        print("YES")
    else:
        print("NO")