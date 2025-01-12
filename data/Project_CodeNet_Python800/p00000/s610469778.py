import itertools

print '\n'.join(['{0}x{1}={2}'.format(i,j,i*j) for i,j in itertools.product(xrange(1,10),repeat=2)])