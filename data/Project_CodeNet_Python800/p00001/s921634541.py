values = []
for i in range(10):
    v = int(input())
    values.append(v)

values.sort(reverse=True)
for i in range(3):
    print(values[i])