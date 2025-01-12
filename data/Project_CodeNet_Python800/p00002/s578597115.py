import sys
print "\n".join(str(len(str(sum(int(x) for x in l.split(' '))))) for l in sys.stdin)