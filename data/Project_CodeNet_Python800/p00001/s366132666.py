H = []
while True:
	try:
		H.append(input())
	except EOFError:
		break
H.sort()
print(H[-1])
print(H[-2])
print(H[-3])