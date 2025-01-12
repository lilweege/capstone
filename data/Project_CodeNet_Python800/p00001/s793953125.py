# Python 3+
#-------------------------------------------------------------------------------
import sys

#ff = open("test.txt", "r")
ff = sys.stdin

arr = [ int(x) for x in ff.readlines() ]

arr.sort(reverse=True)

for x in arr[0:3] : print(x)