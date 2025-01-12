x = 0
y = 0
for i in range(1,10):
    x += 1
    y = 0
    for j in range(1,10):
        y += 1
        print("{}x{}={}".format(x,y,x*y))
