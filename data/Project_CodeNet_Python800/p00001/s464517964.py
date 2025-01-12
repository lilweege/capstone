mtheight = []
 
for i in xrange(0,10):
    mtheight.append(input())
 
mtheight.sort()
for i in xrange(0,3):
    print mtheight[9 - i]