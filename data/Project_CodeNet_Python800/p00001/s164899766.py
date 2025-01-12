a=[]
for i in range(10):
  inp=input()
  a.append(inp)
  if i>=3:
    a.sort()
    del a[0]

print a[2]
print a[1]
print a[0]