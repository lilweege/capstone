L=[]

for i in range(0,10):
    x = raw_input()
    L.append(int(x))
L.sort()

for i in range(0,3):
    print L.pop()