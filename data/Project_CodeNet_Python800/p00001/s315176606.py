import sys

heights = sorted([int(h) for h in sys.stdin], reverse=True)

print(heights[0])
print(heights[1])
print(heights[2])