import sys
for i in sys.stdin.readlines():
    x = i.split(" ")
    print len(str(int(x[0]) + int(x[1])))