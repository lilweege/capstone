m = []
while True:
	try:
		m.append(int(raw_input()))
	except EOFError:
		break
m.sort()
m.reverse()
for h in m[0:3]:
	print h