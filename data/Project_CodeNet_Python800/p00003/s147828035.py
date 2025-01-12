import sys

n=int(input())
for i in range(n):
	list=input().split()
	list=[int(j) for j in list]
	list.sort()
	if list[0]*list[0]+list[1]*list[1]==list[2]*list[2]:
		print("YES")
	else:print("NO")