a=[]
while 1:
    try:
        a.append(int(input()))
    except: break
a.sort(reverse=1)
for i in range(3):print(a[i])