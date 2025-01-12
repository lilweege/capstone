def main():
	import sys

	for line in sys.stdin:
		a, b = map(int, line.split())
		c = a + b
		digits = 1
		while c // 10 != 0:
			c = c // 10
			digits += 1

		print(digits)

if __name__ == '__main__':
	main()