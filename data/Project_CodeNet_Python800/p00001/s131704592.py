a=[]
for i in range(10):
    a.append(int(input()))
a=sorted(a)[::-1]
for i in range(3):
    print(a[i])