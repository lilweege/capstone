x = []
try:
	while True:
		a, b = map(int, raw_input().split())
		x.append(len(list(str(a + b))))
except EOFError:
	for i in x:
		print(i)