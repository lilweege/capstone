res = []
while True:
    try:
        n = input()
        res.append(n)
    except EOFError:
    	break
res.sort()
res = res[len(res)-3:]
for x in reversed(res):
	print x