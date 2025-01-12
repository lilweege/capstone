import sys

for line in sys.stdin:
    datas =line.split()
    if (len(datas)):
        v = int(datas[0]) + int(datas[1])
        print(len(str(v)))
    else:
        break