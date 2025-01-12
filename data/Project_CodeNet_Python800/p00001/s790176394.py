l = []
for i in range(10):
    inp = input()
    l.append(int(inp))
l.sort()
l.reverse()
for i in range(3):
    print(l[i])