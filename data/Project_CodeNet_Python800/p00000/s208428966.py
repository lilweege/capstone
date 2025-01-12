i = range(1,10)
for  i in ['%dx%d=%d' % (x,y,x*y) for x in i for y in i]:
    print i 