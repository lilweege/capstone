l = range(1, 10)
for i in ["%dx%d=%d" % (x, y, x*y) for x in l for y in l]:
    print i