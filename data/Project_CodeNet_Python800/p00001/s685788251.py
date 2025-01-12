#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	mountains = []
	for i in range(10):
		mountains.append(int(input()))
	
	mountains = sorted(mountains, reverse = True)

	for i in range(3):
		print(mountains[i])


if __name__ == '__main__':
    main()