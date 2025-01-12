import sys
a = []
s = sys.stdin.readline()
while s :
	a.append(int(s))
	s = sys.stdin.readline()

a.sort()
a.reverse()
for i in range(3) :
	print(a[i]);