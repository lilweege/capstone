
mons = list()

for i in range(0, 10):
    mons.append(int(input()))
mons = sorted(mons)
for i in range(9, 6, -1):
    print(mons[i])