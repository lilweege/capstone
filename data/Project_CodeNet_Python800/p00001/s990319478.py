#!/usr/bin/python
#-coding:utf8-

import sys

data = map(int,sys.stdin.read().split())
data.sort()
data.reverse()
for s in data[:3]:
  print s