while True:
    try:a,b=map(int,input().split())
    except:break
    c=a+b
    ans=0

    while c>9:
        c=c//10
        ans+=1
    ans+=1
    print(ans)
