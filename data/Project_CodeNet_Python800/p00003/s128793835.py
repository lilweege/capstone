N=input()
for i in range(N):
	a=map(int,raw_input().split())
	a.sort()
	a.reverse()
	if a[0]**2==a[1]**2+a[2]**2:
		print "YES"
	else:
		print "NO"
	
