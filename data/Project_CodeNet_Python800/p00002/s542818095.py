#
# AIZU ONLINE JUDGE: Digit Number
# cf. http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002&lang=jp
#


import sys
import re


#file = open(sys.argv[1], "r")

for line in sys.stdin:
    ab = map(int, re.split(" +", line))
    answer = reduce((lambda x, y: x + y), ab, 0)
    digits = len(str(answer))
    print digits