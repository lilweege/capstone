while 1:
    try:
        x,y = map(int, input().split())
    except EOFError:
        break
    count = 0
    sum = x+y
    while sum > 0:
        sum = sum // 10
        count += 1
    print(count)

