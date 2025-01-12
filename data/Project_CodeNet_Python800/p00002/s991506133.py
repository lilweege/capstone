import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    token = list(map(int, line.strip().split()))
    print(len(str(token[0] + token[1])))