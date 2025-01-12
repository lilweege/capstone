rig=[int(i) for i in input().split(" ")]
while True:
    ke=rig[0]+rig[1]
    ans=1
    count=10
    while True:
        if ke<count:
            print(ans)
            break
        else:
            ans+=1
            count=count*10
    try:rig=[int(i) for i in input().split(" ")]
    except:break