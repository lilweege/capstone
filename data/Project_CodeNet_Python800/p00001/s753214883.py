heightlist = list()
for i in range(10):
	heightlist.append(eval(input()))
heightlist.sort()
for i in range(-1, -4, -1):
	print(heightlist[i])