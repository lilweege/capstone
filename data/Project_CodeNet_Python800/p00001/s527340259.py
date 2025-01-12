values = []
for n in range(10):
    values.append(int(input()))

values.sort(reverse=True)
for v in values[:3]:
    print(v)