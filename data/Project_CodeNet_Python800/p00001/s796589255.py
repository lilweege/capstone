l = []

for i in range(10):
    l.append(int(input()))

l.sort()

for i in range(3):
    print(l[-1 * (i+1)])