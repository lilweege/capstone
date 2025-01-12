a=int(1)
b=int(1)
for i in range(9):
    for o in range(9):
        x=int(a*b)
        print(str(a)+"x"+str(b)+"="+str(x))
        b+=1
    a+=1
    b=1
