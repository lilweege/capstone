import sys
from operator import add

for i in sys.stdin:
    print(len(str(add(*list(map(int, i.split()))))))