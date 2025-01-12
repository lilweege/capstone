import math
import sys

for line in sys.stdin:
    words=line.strip().split(" ")
    a=int(words[0])
    b=int(words[1])
    c=a+b
    if c!=0:
        print(int(1.0000001+math.log(c,10)))
    else:
        print(1)