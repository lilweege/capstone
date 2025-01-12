A=range(1,10)
for i in A:
  x=i
  for j in A:
    print "%dx%d=%d" %(i,j,x)
    x+=i