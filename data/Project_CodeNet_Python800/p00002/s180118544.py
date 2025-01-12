while True:
	try:
		value = input().split(" ")
		result = str(int(value[0]) + int(value[1]))
		print(len(result))
	except EOFError:
		break