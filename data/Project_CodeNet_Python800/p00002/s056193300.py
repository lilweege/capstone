import sys
import math
for line in sys.stdin:
    line = line.strip()
    print int(math.log10(int(line[:line.find(' ')]) + int(line[line.find(' ') + 1:])))+1