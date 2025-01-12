import sys
a = list(map(int,sys.stdin.readlines()))
for i in range(10):
    for j in range(i+1,10):
        if a[i] < a[j]:
            a[i],a[j] = a[j],a[i]
            
for i in range(3):
    print(a[i])