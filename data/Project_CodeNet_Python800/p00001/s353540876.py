#! /usr/bin/python3

m=[int(input()) for i in range(10)]
m.sort()
m.reverse()
print("{0}\n{1}\n{2}".format(m[0], m[1], m[2]))