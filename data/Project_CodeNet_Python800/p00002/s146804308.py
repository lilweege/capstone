# -*- coding: utf-8 -*-
import sys
for s in sys.stdin:
	print len(str(int(s.rstrip().split()[0])+int(s.rstrip().split()[1])))
