while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    count=1
    k=a+b
    while k>=10:
        k//=10
        count+=1
    print(count)