while(True):
	try:
		date=input()
		a,b=map(int,date.split(" "))
		digit=len(str(a+b))
		print(digit)
	except:
		break