heights = list()
for i in range(10):
    heights.append(int(input()))
for height in list(reversed(sorted(heights)))[:3]:
    print(height)