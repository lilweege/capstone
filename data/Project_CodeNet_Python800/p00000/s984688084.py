#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	#print ("x???%d??§???" % x)
	for left in range(1, 10):
		for right in range(1, 10):
			print("{0}x{1}={2}".format(left, right, left * right))

if __name__ == '__main__':
    main()