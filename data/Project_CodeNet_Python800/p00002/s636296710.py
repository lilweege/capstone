while 1:
	try:
		list = str(raw_input()).split()
		x = int(list[0]) + int(list[1])
		print "%d" % len(str(x))

	except:
		break