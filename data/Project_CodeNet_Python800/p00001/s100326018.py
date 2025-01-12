# coding: utf-8

#Name: List of Top 3 Hills
#Level: 1
#Category: ????????????
#Note:

s = [int(raw_input()) for i in range(10)]

s.sort()

for i in range(3):
    print s[9-i]