num1 = 1
num2 = 1
while num1 < 10:
	while num2 < 10:
		print str(num1) + "x" + str(num2) + "=" + str(num1*num2)
		num2 += 1
	num1 += 1
	num2 = 1