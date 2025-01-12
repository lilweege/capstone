a = 1
b = 1

while 2>1:
    print(str(a)+"x"+str(b)+"="+str(a*b))
    if a == 9 and b == 9:
        break
    if b != 9:
        b = b + 1
    else:
        a = a + 1
        b = 1