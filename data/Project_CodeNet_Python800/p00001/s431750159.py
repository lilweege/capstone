heights=[]
for i in range(0,10):
	heights.append(input())
heights.sort()
heights.reverse()
for i in range(0,3):
	print heights[i]