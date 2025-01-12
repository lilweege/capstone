values = []
for i in range(10):
    values.append(int(input()))

top3 = []
for i in range(3):
    Max = max(values)
    top3.append(Max)
    values.remove(Max)

for x in top3:
    print(x)