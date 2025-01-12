import sys
L = sys.stdin.readlines()
for line in L:
	N = line[:-1].split(' ')
	sums = int(N[0]) + int(N[1])
	print(len(str(sums)))