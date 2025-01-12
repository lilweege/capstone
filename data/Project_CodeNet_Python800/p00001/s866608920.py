arr = []
for i in range(10):
	arr=arr+[int(raw_input())]
arr.sort()
arr.reverse()
for i in range(3):
	print(arr[i])