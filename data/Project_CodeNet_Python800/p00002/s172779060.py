while True:
	try:
		[a, b] = map(int, raw_input().split())
		sum = a + b
		count = 0
		while sum:
			count += 1
			sum /= 10
		print count
	except (EOFError):
		break;