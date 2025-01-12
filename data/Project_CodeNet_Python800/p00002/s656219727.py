#!/usr/bin/python
import sys

for l in sys.stdin:
    array = l.split()
    print len(str(int(array[0]) + int(array[1])))