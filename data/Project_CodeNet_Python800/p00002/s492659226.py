import sys
for line in sys.stdin:
	l=0
	for l in range(len(line)):
		if(line[l] == ' '):
			p = l
			break
	a = line[0:p]
	b = line[p+1:]
	c = int(a)+int(b)
	d = 1
	while(int(c/10) != 0):
		d += 1
		c = int(c/10)
	print(d)
