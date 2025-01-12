# -*- config: utf-8 -*-
if __name__ == '__main__':
	while 1:
		try:
			nums = map(int,raw_input().split())
			s = sum(nums)
			print len(str(s))
		except:
			break