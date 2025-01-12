high=[0 for i in range(10)]
for i in range(10):
	high[i]=int(input())
	
ans=[0 for i in range(3)]
for i in range(3):
	ans[i]=max(high)
	high.remove(ans[i])
	print(ans[i])