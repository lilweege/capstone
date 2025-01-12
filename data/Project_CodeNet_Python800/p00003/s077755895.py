def pascal(xdata):
	for x in xrange(3):
		for y in xrange(3):
			for z in xrange(3):
				if xdata[x]**2 + xdata[y]**2 == xdata[z]**2:
					return True
	return False

N = input()
data = [map(int, raw_input().split()) for x in range(N)]

for x in data:
	if pascal(x):
		print "YES"
	else:
		print "NO"