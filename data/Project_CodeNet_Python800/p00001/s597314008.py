import sys
heights = []
for l in sys.stdin:
  heights.append(int(l))
heights = sorted(heights, reverse=True)
print(heights[0])
print(heights[1])
print(heights[2])