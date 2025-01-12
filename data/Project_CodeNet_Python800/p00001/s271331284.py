p1 = 0
p2 = 0
p3 = 0
for i in range(10):
    d = int(raw_input())
    if (d > p1):
        p3 = p2
        p2 = p1
        p1 = d
    elif (d > p2):
        p3 = p2
        p2 = d
    elif (d > p3):
        p3 = d

print p1
print p2
print p3