heightOfMountains = []
for i in range(1, 11):
	heightOfMountains.append(int(input()))
heightOfMountains.sort()
for i in range(1, 4):
	print(heightOfMountains[-i])