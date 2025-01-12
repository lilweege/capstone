
mt=[]
high=[0,0,0]
for i in range(10):
    mt.append(int(input()))
    if  mt[i] > high[0]:
        high=[mt[i]]+high[:2]
    elif mt[i] > high[1]:
        high=[high[0]]+[mt[i]]+[high[1]]
    elif mt[i] > high[2]:
        high=high[:2]+[mt[i]]
print ('\n'.join(map(str,high)))