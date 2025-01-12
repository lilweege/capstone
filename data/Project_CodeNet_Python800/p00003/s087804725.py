N = input()
a = []
for i in range(N):
	a = map(int, raw_input().split())
	b = [0]
	for i in a:
		j = 0
		while j < 3:
			if i > b[j]:
				b.insert(j, i)
				break
			j += 1
	if b[0]**2 == b[1]**2 + b[2]**2:
		print "YES"
	else:
		print "NO"