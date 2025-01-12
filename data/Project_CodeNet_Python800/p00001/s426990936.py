mount=[]
for i in range(10):
  tmp=int(input())
  mount.append(tmp)
mount.sort()
mount.reverse()
for i in range(3):
    print(mount[i])