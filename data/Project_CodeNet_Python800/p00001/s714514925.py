import sys

a = []
for i in range(10):
    a.append(int(input()))
#num = [1819, 2003, 876, 2840, 1723, 1673, 3776, 2848, 1592, 922]
a.sort(reverse = True)
print(a[0])
print(a[1])
print(a[2])