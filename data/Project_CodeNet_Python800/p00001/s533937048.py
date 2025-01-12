a = [0]
for i in range(10):
    if i == 0:
        a[0] = input()
    else:
        a.append(input())
else:
    a.sort()
    a.reverse()
    print a[0]
    print a[1]
    print a[2]