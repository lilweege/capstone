
l = []
for i in range(0,10):
    l.append(int(input()))

l.sort(reverse=True)
l=l[:3]
for j in l:
    print(j)