heights = [int(input()) for i in range(0, 10)]
heights.sort(reverse=True)
for height in heights[:3]:
    print(height)