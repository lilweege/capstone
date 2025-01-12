heights = []
for i in range(10):
    heights.append(int(input()))

for i in range(10):
    for j in range(i,10):
        if (heights[j] > heights[i]):
            w = heights[i]
            heights[i] = heights[j]
            heights[j] = w

for i in range(3):
    print(heights[i])