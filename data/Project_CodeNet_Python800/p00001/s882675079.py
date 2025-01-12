def ListofTopHills():
    h=[]
    for i in range(10):
        h.append(int(input()))
    h=sorted(h)

    for i in range(3):
        print(h[9-i])
        
ListofTopHills()