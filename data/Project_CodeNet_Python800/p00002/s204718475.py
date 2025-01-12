import sys
for line in sys.stdin:
    print(len(str(sum(list(map(int, line.split()))))))