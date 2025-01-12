mountains = []
for n in range(10):
	mountains.append(int(input()))

mountains.sort()
mountains.reverse()

for n in [0,1,2]:
	print(mountains[n])