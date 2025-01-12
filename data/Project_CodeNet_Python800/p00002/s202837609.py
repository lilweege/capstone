import sys
[print(len(str(sum(map(int, line.split()))))) for line in sys.stdin]