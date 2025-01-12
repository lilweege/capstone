lis=list()

for a in range(1,11):
    num=int(input())
    lis.append(num)

lis.sort()
for va in range(9,6,-1):
    print(lis[va])