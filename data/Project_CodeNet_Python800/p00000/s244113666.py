# Aizu Problem 0000: QQ
#
import sys, math, os

# read input:
#PYDEV = os.environ.get('PYDEV')
#if PYDEV=="True":
#    sys.stdin = open("sample-input2.txt", "rt")

for i in range(1, 10):
    for j in range(1, 10):
        print("%dx%d=%d" % (i, j, i*j))