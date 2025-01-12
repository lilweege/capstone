line_num = int(raw_input())
for n in range(line_num):
	a,b,c = map(int, raw_input().split(" "))
	if a>b:
		if a>c:
			if a*a == b*b + c*c:
				print "YES"
				continue
		else:
			if c*c == a*a + b*b:
				print "YES"
				continue
	else:
		if b>c:
			if b*b == a*a + c*c:
				print "YES"
				continue
		else:
			if c*c == a*a + b*b:
				print "YES"
				continue
	print "NO"