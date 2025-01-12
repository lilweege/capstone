ans_list=[]
while True:
	try:
		k=list(map(int,input().split(" ")))
		ans_list.append(k[0]+k[1])
	except:
		for i in ans_list:
			print(len(str(i)))
		break