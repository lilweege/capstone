for val in range(input()):
    x = map(int,raw_input().split(' '))
    x.sort()
    if x[0]**2+x[1]**2==x[2]**2: print 'YES'
    else: print 'NO'