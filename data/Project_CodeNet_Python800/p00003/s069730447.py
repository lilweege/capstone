n = int(input())
for i in range(n):
    s = input().split(" ")
    s = [int(j) for j in s]
    s.sort()
    a = s[0]
    b = s[1]
    c = s[2]

    if(a**2+b**2==c**2):
        print("YES")
    else:
        print("NO")