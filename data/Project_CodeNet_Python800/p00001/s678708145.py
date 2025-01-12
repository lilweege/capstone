heights = []
for i in range(10):
    heights.append(int(input()))

for i in range(10):
    for j in range(i,10):
        if (heights[j] > heights[i]):
            w = heights[i]
            heights[i] = heights[j]
            heights[j] = w

print(heights[0])
print(heights[1])
print(heights[2])