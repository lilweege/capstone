a = []
for i in range(10):
    a.append(input())
a = sorted(a, key=int, reverse=True)
for i in a[0:3]:
    print(i)