M = [0 for i in xrange(10)]

for i in xrange(10):
    M[i] = int(raw_input())
    
M.sort()
M.reverse()

for i in xrange(3):
    print M[i]