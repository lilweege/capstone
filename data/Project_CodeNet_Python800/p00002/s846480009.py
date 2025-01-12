import sys;

for line in sys.stdin:
	a = [int(num) for num in line.split()];
	sum = a[0] + a[1];
	count = 0;
	while sum > 0:
		count += 1;
		sum //= 10;
	print(count);