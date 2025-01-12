import sys
import math

while True:
    line = sys.stdin.readline()
    if not line:
        break
    token = list(map(int, line.strip().split()))
    print(int(math.log10(token[0] + token[1]) + 1))