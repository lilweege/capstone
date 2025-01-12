def digit(n):
	cnt = 1
	m = n

	while 10 <= m:
		cnt += 1
		m = m / 10
		
	return cnt

while True:
	try:
		inpt = map(int, raw_input().split())
		print digit(inpt[0]+inpt[1])

	except:
		break