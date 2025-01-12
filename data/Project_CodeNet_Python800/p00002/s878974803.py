import sys

lines = []
for line in sys.stdin:
    num = line.split(" ")
    print(len(str(int(num[0]) + int(num[1]))))