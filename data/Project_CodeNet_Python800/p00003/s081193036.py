
def check(a, b, c):

    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2

    if (a2 + b2) == c2:
        return True
    else:
        return False


n = int(input())

for c in range(n):
    line = input()
    datas = map(int, line.split())
    li = list(datas) 
    a = li[0]
    b = li[1]
    c = li[2]

    if check(a, b, c) or check(b, c, a) or check(c, a, b):
        print("YES")
    else:
        print("NO")