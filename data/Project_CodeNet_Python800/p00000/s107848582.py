import itertools

for i,j in itertools.product(xrange(1,10),repeat=2):
	print '{0}x{1}={2}'.format(i,j,i*j)