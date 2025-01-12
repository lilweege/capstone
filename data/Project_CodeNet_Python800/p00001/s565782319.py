data = []
for i in range(1,11):
	h = int(input())
	data.append(h)

for i in sorted(data)[::-1][0:3]:
	print(i)