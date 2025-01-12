a = []
for i in range(10):
    a.append(int(input()))
a.sort()
print("\n".join(list(map(str,a[9:6:-1]))))