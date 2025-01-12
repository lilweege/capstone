import sys
[print(len(str(sum([int(y) for y in x.split(" ")])))) for x in sys.stdin]