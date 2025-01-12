import sys
import math
for n in [int(math.log10(float(int(line.split()[0])+int(line.split()[1]))))+1 for line in sys.stdin]:
	print n