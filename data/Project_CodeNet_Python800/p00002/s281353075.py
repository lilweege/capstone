import sys
for line in sys.stdin:
	a = int(line.split()[0])
	b = int(line.split()[1])
	s = a + b
	print(len(str(s)))