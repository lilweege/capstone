height = []
for i in range(10):
    height.append(input())
height.sort(reverse=True)
for i in range(3):
    print(height[i])