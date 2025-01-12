n = input()
for i in xrange(n):
    li = map(int, raw_input().split())
    li.sort()    
    if li[0]**2 + li[1]**2 == li[2]**2:
        print "YES"
    else:
        print "NO"