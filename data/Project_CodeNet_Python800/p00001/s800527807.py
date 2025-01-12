lis=[];

for i in range(10):
    h=int(input());
    lis.append(h);
    
for i in range(10):
    for j in range(i+1,10):
        if lis[i]<lis[j]:
            a=lis[i];
            lis[i]=lis[j];
            lis[j]=a;
            
for i in range(3):
    print(lis[i]);