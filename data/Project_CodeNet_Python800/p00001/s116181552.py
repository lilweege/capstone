a = [0, 0, 0, 0]
for t in range(10):
    a[3] = input()
    for i in range(2, -1, -1):
        if (a[i] < a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]

for i in range(0, 3):
    print a[i]