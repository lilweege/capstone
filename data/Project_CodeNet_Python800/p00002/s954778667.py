import sys

[print(len(str(sum([int(j) for j in i.split()])))) for i in sys.stdin]