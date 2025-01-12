
mountain = []

for _ in range(10):
	mountain.append(int(input()))
	
mountain.sort()
mountain.reverse()

print(mountain[0])
print(mountain[1])
print(mountain[2])