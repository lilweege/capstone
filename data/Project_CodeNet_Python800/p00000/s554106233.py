calc = "{}x{}={}"

for i in range(1,10):
    for j in range(1,10):
        print(calc.format(i,j,i*j))