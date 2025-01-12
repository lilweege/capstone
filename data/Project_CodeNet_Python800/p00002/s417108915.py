while True:
    try:
        s=input().split(" ")
        num=int(s[0])+int(s[1])
        print(len(str(num)))
    except:
        break
   