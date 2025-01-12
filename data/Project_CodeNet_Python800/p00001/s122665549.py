a=[]
for i in range(1,11):
    b=int(input())
    a.append(b)
a.sort(reverse=True)
for i in range(3):
    print(a[i])