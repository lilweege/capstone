# Aizu Problem 0002: Digit Number
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


for line in sys.stdin:
    a, b = [int(_) for _ in line.split()]
    print(len(str(a + b)))