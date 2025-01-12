a = []
for i in range(10):
    a.append(int(raw_input()))
a.sort()
a.reverse()
for i in range(3):
    print a[i]