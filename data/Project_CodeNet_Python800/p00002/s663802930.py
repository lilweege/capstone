import sys
c=[len(str(sum(map(int,line.split())))) for line in sys.stdin]
[print(i) for i in c]

