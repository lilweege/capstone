x = 1
y = 1

for x in range(9):
    for y in range(9):
        print((x+1),"x",(y+1),"=",(x+1)*(y+1),sep="")
        y = y + 1
        
    x = x + 1
