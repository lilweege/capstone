import sys

list = []

for i in range(10):
    list.append(input())

list.sort()
list.reverse()

print list[0]
print list[1]
print list[2]