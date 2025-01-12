# -*- config: utf-8 -*-
if __name__ == '__main__':
	for i in range(int(raw_input())):
		nums = map(lambda x:x**2,map(int,raw_input().split()))
		flg = False
		for i in range(3):
			s = int(0)
			for j in range(3):
				if i == j :
					continue
				s += nums[j]
			if s == nums[i] :
				flg = True

		if flg == True :
			print "YES"
		else :
			print "NO"