import sys
for x in xrange(1,10):
	for y in xrange(1,10):
		sys.stdout.write("%dx%d=%d\n"%(x,y,x*y))