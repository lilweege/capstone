height=[]
for i in xrange(10):
    mountain=input()
    height.append(mountain)
height.sort()
height.reverse()
for i in xrange(3):
    print(height[i])