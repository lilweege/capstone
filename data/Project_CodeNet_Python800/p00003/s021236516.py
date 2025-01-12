N = int(input())

for i in range(N):
	num = sorted(map(int, input().split()))
	if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
		print("YES")
	else:
		print("NO")