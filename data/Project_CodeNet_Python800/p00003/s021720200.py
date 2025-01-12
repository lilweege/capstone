
N = input()

a = []
for i in range(int(N)):
    s = input().split()
    ss = [int(s[0]), int(s[1]), int(s[2])]
    ss.sort()

    if ss[2]**2 == ss[0]**2 + ss[1]**2:
        print("YES")
    else:
        print("NO")