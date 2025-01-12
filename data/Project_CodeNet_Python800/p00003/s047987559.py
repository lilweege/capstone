import sys
size = int(sys.stdin.readline())
for i in range(size):
    line = sys.stdin.readline()
    line = line.split(" ")
    inp = []
    for j in line:
        inp.append(int(j))
    inp.sort()
    if (inp[0]**2+inp[1]**2==inp[2]**2):
        print("YES")
    else:
        print("NO")