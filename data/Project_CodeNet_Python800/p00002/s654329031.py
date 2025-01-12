import sys

data = []
for i in sys.stdin:
    data.append(list(map(int, i.split())))

for j in range(len(data)):
    print(len(str(data[j][0] + data[j][1])))