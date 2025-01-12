# Aizu Problem 0001: List of Top 3 Hills
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


for h in sorted([int(input()) for _ in range(10)], reverse=True)[:3]:
    print(h)