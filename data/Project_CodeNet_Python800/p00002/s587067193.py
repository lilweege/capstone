while True:
	try:
		a, b = map(int, raw_input().strip().split(' '))
		c = a + b
		ans = 0
		while c > 0:
			ans += 1
			c /= 10
		print ans
	except EOFError:
		break