mountain=[]
for s in range(0,10):
    mountain.append(int(input()))
mountain.sort(reverse=True)
for s in range(0,3):
 print(mountain[s])