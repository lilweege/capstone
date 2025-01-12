#!/usr/bin/python
#-coding:utf8-

import sys

for s in sys.stdin:
  data = map(int,s.split())
  print len(str(data[0]+data[1]))