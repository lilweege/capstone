#!/usr/bin/env python3
hight = []
for i in range(10):
    hight.append(int(input()))
hight = sorted(hight, reverse=True)

for i in range(3):
    print(hight[i])