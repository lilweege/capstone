a = 1
b = 1
while True:
	if a != 10:
		while True:
			print(str(a) + 'x' + str(b) + '=' + str(a*b))
			b += 1
			if b != 10:
				continue
			else:
				b = 1
				a += 1
				break
		continue
	else:
		break