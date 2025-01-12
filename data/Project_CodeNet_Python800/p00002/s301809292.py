l = list(map(int, input().split()))

while(l != []):
    try:
        length = len(str(l[0]+l[1]))
        print(length)
        l = list(map(int, input().split()))
    except:
        break
