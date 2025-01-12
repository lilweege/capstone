a=[]

for i in range(0,10):
    a.append(input())
inp = list(map(int,a))

INP=[0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
    for j in range(i+1,10):
        if inp[i]<inp[j]:
            INP[j]+=1
        elif inp[i]>inp[j]:
            INP[i]+=1
        else:
            INP[i]+=1
            INP[j]+=1

z = 0

for i in range(9,-1,-1):
    if z >= 3:
        break
    for j in range(0,10):
        if i == INP[j]:
            print(inp[j])
            z+=1
        if z >= 3:
            break