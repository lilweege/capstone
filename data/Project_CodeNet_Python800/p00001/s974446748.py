heights = [int(input()) for n in xrange(10)]
for x in xrange(3):
    v = max(heights)
    print v
    heights.remove(v)