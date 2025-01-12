a = 1; b = 1

while True:
    print(a,"x",b,"=",a*b,sep="")
    b += 1
    if b == 10:
        a += 1; b = 1
        if a == 10:
            break
