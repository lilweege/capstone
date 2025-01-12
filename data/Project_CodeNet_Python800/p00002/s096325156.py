#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	while True:		
		try:
			num = eval(input().replace(" ","+"))
		except:
			return
		else:
			print(len(str(num)))
if __name__ == '__main__':
  main()