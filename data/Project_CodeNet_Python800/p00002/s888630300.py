res=[]

while 1:
    try:
        s=input()
        a,b = [int(x) for x in s.split()]
        res.append(a+b)
    except:
        for n in res:
            print(len(str(n)))
        break