from itertools import product

for i in product(list(range(1,10)),list(range(1,10))):
    print(i[0],"x",i[1],"=",i[0]*i[1],sep="")