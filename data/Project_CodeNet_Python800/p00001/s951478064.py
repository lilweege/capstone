# coding: utf-8
# Here your code !
import sys
line = sys.stdin.readlines()
top = [0,0,0]
for i in range(len(line)):
    line[i] = int(line[i].rstrip("\n"))
    if top[0] < line[i]:
        top[2] = top[1]
        top[1] = top[0]
        top[0] = line[i]
    elif top[1] < line[i]:
        top[2] = top[1]
        top[1] = line[i]
    elif top[2] < line[i]:
        top[2] = line[i]

for i in range(3):
    print(top[i])