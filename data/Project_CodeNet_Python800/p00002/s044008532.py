#@ /usr/bin/env python3.4
import sys
list = sys.stdin.readlines()
for i in list:
    num = i[:-1].split(' ', 2)
    print(len(str(int(num[0])+int(num[1]))))