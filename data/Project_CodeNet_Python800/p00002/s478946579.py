import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.split(" ")
    inp = []
    for i in line:
        inp.append(int(i))
    print (len(str(inp[0]+inp[1])))