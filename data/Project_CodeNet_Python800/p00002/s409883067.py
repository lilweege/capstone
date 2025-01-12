#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
	a,b = line.split(' ')
	value = int(a) + int(b)
	print( len('{}'.format(value)) )