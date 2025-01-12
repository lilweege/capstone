n = list()

for var in range(0,10):
	n.append(int(input()))

n.sort(reverse=True)

for i in n[:3]:
	print(i)