import sys
while(True):
    try:
        a,b=[int(i) for i in input().split()]
        print(len(str(a+b)))
    except:
        sys.exit()