h = []
for i in range(10):
    h.append(int(input()))

max1 = max(h)
h.remove(max1)
max2 = max(h)
h.remove(max2)
max3 = max(h)

print(max1)
print(max2)
print(max3)