import sys

a = ""
for input in sys.stdin:
    a += input
l = a.split()
for i in range(0,len(l),2):
    print len(str(int(l[i])+int(l[i+1])))
