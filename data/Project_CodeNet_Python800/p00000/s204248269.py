x = 0
y = 0
z = 0
for i in range(9):
	x += 1
	y = 0
	for j in range(9):
		y += 1
		z = x*y
		print(x, end = 'x')
		print(y, end = '=')
		print(z)