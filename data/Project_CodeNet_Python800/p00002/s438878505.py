while True:
	try:
		a=input().split()
	except:
		break
	b=int(a[0])+int(a[1])
	print(len(str(b)))