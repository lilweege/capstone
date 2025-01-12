A=[1,2,3,4,5,6,7,8,9]
for i in A:
    for j in A:
        print(i, end="x")
        print(j, end="=")
        print(i*j)