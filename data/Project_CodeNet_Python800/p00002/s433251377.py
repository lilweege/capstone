while True:
	try:
		a = raw_input()
		temp = a.split()
		x = int(temp[0]) + int(temp[1])
		c = str(x)
		print len(c)
	
	except:
		break