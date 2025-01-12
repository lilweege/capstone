N=int(input())
for n in range(N):
	sides = list(map(int,input().split()))
	sides.sort()
	if sides[-1]**2 == sides[-2]**2 + sides[-3]**2:
		print("YES")
	else:
		print("NO")