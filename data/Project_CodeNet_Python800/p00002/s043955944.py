import sys

for line in sys.stdin:
	list = line.split()
	print len(str(eval(list[0])+eval(list[1])))