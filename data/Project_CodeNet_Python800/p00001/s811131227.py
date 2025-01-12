f=s=t=0
for i in range(10):
    n=int(input())
    if(n > f):
        t = s
        s = f
        f = n
    elif(n > s):
        t = s
        s = n
    elif(n > t):
        t = n
print('%d\n%d\n%d'%(f,s,t))