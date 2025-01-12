import itertools
def check(a,b,c):
    for p in itertools.permutations([a,b,c]):
        (x,y,z)=p
        if x*x+y*y==z*z:
            return True
    return False

n=input()
for i in range(n):
    (a,b,c)=map(eval,raw_input().split())
    if check(a,b,c):
        print "YES"
    else:
        print "NO"