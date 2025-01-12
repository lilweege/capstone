def kakezan(a,b):
    A = a*b
    return A

for j in range(9):
    for i in range(9):
        print(j+1,"x",i+1,"=",kakezan(j+1,i+1),sep="")
