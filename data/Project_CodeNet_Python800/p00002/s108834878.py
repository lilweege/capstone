import sys
a=[map(int,i.split()) for i in sys.stdin]
[print(len(str(b+c))) for b,c in a]