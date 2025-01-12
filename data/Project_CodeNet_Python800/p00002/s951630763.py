import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    print(len(str(abs(sum(map(int, line.rstrip().split(' ')))))))