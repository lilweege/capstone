import sys,math
for x,y in (line.split() for line in sys.stdin):print(int(math.log10(int(x)+int(y))+1))