a = []
for i in range(10):
    a.append(int(input()))
for i in sorted(a)[-1:-4:-1]:
    print(i)