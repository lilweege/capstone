import sys;

for line in sys.stdin:
	n = int(line);
	for i in range(0, n):
		a = [int(num) for num in input().split()];
		a.sort();
		if a[2] ** 2 == (a[0] ** 2) + (a[1] ** 2):
			print('YES');
		else:
			print('NO');