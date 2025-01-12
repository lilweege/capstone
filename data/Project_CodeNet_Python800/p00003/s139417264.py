count=int(raw_input())

for i in range(0,count):
    a,b,c=map(int,raw_input().split())
    if pow(a,2)+pow(b,2)==pow(c,2):
        print 'YES'
    elif pow(a,2)+pow(c,2)==pow(b,2):
        print 'YES'
    elif pow(b,2)+pow(c,2)==pow(a,2):
        print 'YES'
    else:
        print 'NO'