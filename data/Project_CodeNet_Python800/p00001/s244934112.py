a=[int(input()) for i in range(10)]
a.sort(reverse=True)
for i, iv in enumerate(a):
	print(iv)
	if i >= 2:
		break