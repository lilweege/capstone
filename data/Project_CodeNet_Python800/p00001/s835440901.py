# -*- coding:utf-8 -*-

first = 0
second = 0
third = 0
i = 0

for i in range(0,10):
    line = int(input())
    
    if first < int(line):
        third = second
        second = first
        first = int(line)
    elif second < int(line):
        third = second
        second = int(line)
    elif third < int(line):
        third = int(line)
print(first)
print(second)
print(third)