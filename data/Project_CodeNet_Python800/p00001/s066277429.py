height_list = []
for i in range(10):
    height_list.append(input())
height_list.sort()
height_list.reverse()

for height in height_list[:3]:
    print height