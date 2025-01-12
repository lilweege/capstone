import sys

for i in sys.stdin.readlines():
    a, b = map(int, i.strip().split())
    print "{0}".format(len(str((a + b))))