for ii in xrange(1,10):
    for jj in xrange(1,10):
        # print(str(ii) + "x" + str(jj) + "=" + str(ii * jj))
        data = (ii, jj, ii * jj, )
        print("%dx%d=%d" % data)