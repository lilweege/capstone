data = []
for i in range(10):
    data.append(int(input()))
    
sdata = sorted(data)
for i in range(3):
    print(sdata[9-i])