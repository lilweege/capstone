import sys

for i in sys.stdin:
    print(len(str(sum(map(int,i.replace("\n", "").split(" "))))))