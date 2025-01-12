L = []
for _ in range(10):
    L.append(int(input()))
L.sort(reverse=True)
for m in L[:3]:
    print(m)