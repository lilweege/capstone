def counts(num):
	countlist.append(len(str(num[0] + num[1])))

countlist = []
flag = True
while flag :
	try:
		counts(map(int, raw_input().split()))
	except:
		flag = False
		for x in countlist:
			print x