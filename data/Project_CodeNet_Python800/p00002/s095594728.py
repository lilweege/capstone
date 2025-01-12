while True:
	try:
		a,b = map(int,raw_input().split(' '))
		print len(str(a+b))
	except: break