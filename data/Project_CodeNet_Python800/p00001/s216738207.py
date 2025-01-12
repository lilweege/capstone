a=[]
for i in range(10):
    a.append(input())
a.sort()
a=a[::-1]
a=a[:3]
print(a[0])
print(a[1])
print(a[2])