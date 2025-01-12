import sys

#list = sys.stdin.readlines()

#i=0
list = []
for line in sys.stdin.readlines():
	list = line.split(" ")
	print str(len(str(int(list[0]) + int(list[1]))))