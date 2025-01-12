for a,b,c in[sorted(map(int,raw_input().split()))for i in range(input())]:
	print"NO"if c*c-a*a-b*b else"YES"