# -*- config: utf-8 -*-
if __name__ == '__main__':
	hills = []
	for i in range(10):
		tmp = raw_input()
		hills.append(int(tmp))
	hills.sort(reverse=True)

	for i in range(3):
		print hills[i]