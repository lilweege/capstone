mnts = []
for t in xrange(0, 10):
	mnts.append(int(raw_input()))
tops = sorted(mnts, reverse = True)
for i in xrange(0, 3):
	print tops[i]