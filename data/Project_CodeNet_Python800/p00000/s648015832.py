from itertools import product
for i,j in product(range(1,10),range(1,10)):
 print("{}x{}={}".format(i,j,i*j))