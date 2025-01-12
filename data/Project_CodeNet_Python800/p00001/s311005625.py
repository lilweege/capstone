a = [int(input()) for i in range(10)]

a.sort()

for i in range(1, 4):
    print(a[-i])