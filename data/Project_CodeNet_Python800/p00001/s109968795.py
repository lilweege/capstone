mount = []

for i in range(0, 10):
    n = input()
    mount.append(n)

mount.sort(reverse = True)

for i in range(0, 3):
    print mount[i]