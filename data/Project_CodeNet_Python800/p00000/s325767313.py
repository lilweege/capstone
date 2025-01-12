#coding:utf-8

import itertools
r = range(1,10)
for (x,y) in itertools.product(r,r):
	print('{}x{}={}'.format(x,y,x*y))