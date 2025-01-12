lis=[]
for i in range(10):
  lis.append(int(input()))
 
for i in sorted(lis,reverse=True)[:3]:
  print(i)