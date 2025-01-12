import sys
a=[]
for i in sys.stdin:
    a.append(map(int,i.split()))
for i in a:
    print(str(len(str(i[0]+i[1]))))