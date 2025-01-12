x = input()
for i in xrange(x):
    inp = map(int ,raw_input().split())
    inp.sort()

    if inp[2]**2 == inp[0]**2 + inp[1]**2:
        print "YES"
    else:
        print "NO"