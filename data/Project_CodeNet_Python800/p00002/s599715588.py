l = []
while True:
    try:
        (a,b) = input().split(" ")
        l.append((int(a) + int(b)))
    except:
        break  
for i in l:
    print(len(str(i)))