import sys
import math

n = int(input())
for i in range(n):
	a = list(map(int, input().split()))
	a.sort()

	if a[0]**2 + a[1]**2 == a[2]**2:
		print('YES')
	else:
		print('NO')