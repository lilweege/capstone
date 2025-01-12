N = int(input())

for i in range(N):
	sides = list(map(int, input().split()))
	longestSide = max(sides)
	sides.remove(longestSide)
	if (longestSide ** 2) == (sides[0] ** 2 + sides[1] ** 2):
		print('YES')
	else:
		print('NO')