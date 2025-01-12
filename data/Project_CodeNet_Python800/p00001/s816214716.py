L=list(range(10))
for i in range(10):
    L[i]=int(input())
print(max(L))
L.remove(max(L))
print(max(L))
L.remove(max(L))
print(max(L))