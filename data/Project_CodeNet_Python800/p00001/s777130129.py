import sys
m = [int(l) for l in sys.stdin]
m.sort()
print(m[-1])
print(m[-2])
print(m[-3])