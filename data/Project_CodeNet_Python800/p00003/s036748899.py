n = int(raw_input())

for i in range(n):
	temp = [int(x) for x in raw_input().split()]
	temp.sort(reverse = True)

	if temp[0] ** 2 == temp[1] ** 2 + temp[2] ** 2:
		print "YES"
	else:
		print "NO"