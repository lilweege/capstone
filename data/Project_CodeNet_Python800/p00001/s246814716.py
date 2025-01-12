m1=m2=m3=0
for i in range(10):
    m3=max(m3,int(input()))
    if m3>m2:m2,m3=m3,m2
    if m2>m1:m1,m2=m2,m1
print(m1)
print(m2)
print(m3)
