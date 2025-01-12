hillheight = []
for i in range(0, 10):
	hillheight.append(int(raw_input()))

hillheight.sort()

for i in range(0, 3):
	print(hillheight[-1-i])