a = []
for i in range(10):
    a.append(int(input()))
a.sort()
for j in range(3):
    print(a[-(j+1)])