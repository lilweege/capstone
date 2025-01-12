a = [x for x in range(9)]

for i in a:
    for j in a:
        print("{}x{}={}".format(i+1,j+1,(i+1)*(j+1)))