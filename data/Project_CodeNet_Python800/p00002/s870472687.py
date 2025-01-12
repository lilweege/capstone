# Digit Number

import sys

results = []

for line in sys.stdin:
	results.append(int(line.split()[0]) + int(line.split()[1]))

for result in results:
	print len(str(result))