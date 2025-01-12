while True:
    try:a,b=map(int,input().split())
    except:break
    if a=="" or b==":":
        break
    c=a+b
    ans=0
    if c>=0 and c<=9:
        ans=1
    if c>=10 and c<=99:
        ans=2
    if c>=100 and c<=999:
        ans=3
    if c>=1000 and c<=9999:
        ans=4
    if c>=10000 and c<=99999:
        ans=5
    if c>=100000 and c<=999999:
        ans=6
    if c>=1000000 and c<=9999999:
        ans=7

    print(ans)
