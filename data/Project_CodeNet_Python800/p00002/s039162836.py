import sys
l = []
for line in sys.stdin:
    l.append(line)

for i in range(len(l)):
    numl = l[i].split(' ')
    a = int(numl[0])
    b = int(numl[1])
    sum = a + b
    digitstr = "{0}".format(sum)
    print(len(digitstr))