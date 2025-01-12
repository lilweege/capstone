import sys
heights = []
for i in range(10):
    line = sys.stdin.readline()
    height = int(line)
    heights.append(height)
heights.sort()
heights.reverse()
for i in range(3):
    print (heights[i])