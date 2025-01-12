def solve():
	a,b = map(int,input().split())
	print(len(str(a+b)))

while True:
	try:
		solve()
	except:
		break