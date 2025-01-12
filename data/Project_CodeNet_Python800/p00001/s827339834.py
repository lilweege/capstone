import sys

#list = sys.stdin.readlines()

i=0
list = []
for line in sys.stdin.readlines():
	list.append(int(line.strip("\n")))

print sorted(list, reverse=True)[0]
print sorted(list, reverse=True)[1]
print sorted(list, reverse=True)[2]