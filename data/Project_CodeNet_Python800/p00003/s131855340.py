times = int(input())

for i in range(0, times):
	edge = []
	for e in input().split(" "):
		edge.append(int(e))
	edge.sort()
	if pow(int(edge[0]), 2) + pow(int(edge[1]), 2) == pow(int(edge[2]), 2):
		print("YES")
	else:
		print("NO")