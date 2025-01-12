height =[]
inp = ""
for i in range(0,10):
    inp = input()
    height.append(int(inp))
height.sort(reverse=True)
for i in range(0,3):
    print(str(height[i]))