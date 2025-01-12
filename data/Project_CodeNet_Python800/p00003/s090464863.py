n=input()
for i in range(n):
	l=map(int,raw_input().split())
	l.sort()
	if l[0]**2+l[1]**2==l[2]**2:print"YES"
	else:print"NO"