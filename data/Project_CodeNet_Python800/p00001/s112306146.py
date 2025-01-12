import sys

heights = []

for height in sys.stdin:
  heights.append(int(height.rstrip()))

heights.sort()
heights.reverse()

for i in range(3):
  print heights[i]