#a=list(map(int,input().split()))
a=[]
for i in range(10):
    tmp = int(input())
    a.append(tmp)
b=sorted(a, reverse=True)
print(b[0])
print(b[1])
print(b[2])