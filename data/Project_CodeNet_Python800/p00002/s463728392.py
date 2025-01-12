import sys,math

inputs = list()

for n in sys.stdin:
	inputs.append(list(map(int,n.split())))

for n in inputs:
	print(math.floor(math.log10(n[0]+n[1]))+1)