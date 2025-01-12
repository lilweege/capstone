# -*- coding: utf-8 -*-
import math
num = int(raw_input())
for i in range(num):
    list = [int(x) for x in raw_input().split(" ")]
    list.sort(lambda n1, n2:n2 - n1)
    if list[0]**2 == list[1]**2 + list[2]**2:
        print("YES")
    else:
        print("NO")