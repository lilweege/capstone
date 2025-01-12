import sys
# l = sys.stdin.readline()
l = sys.stdin.readlines()
for line in l:
    data = map(int, line.split(" "))
    print(len(str(data[0] + data[1])))