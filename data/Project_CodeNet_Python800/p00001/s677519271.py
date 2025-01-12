a=[]
for i in range(10):
    num = int(input())
    a.append(num)
a=sorted(a)
for i in range(3):
    print('{0}'.format(a[9-i]))