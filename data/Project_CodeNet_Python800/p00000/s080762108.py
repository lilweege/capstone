# -*- coding: utf-8 -*-

func = lambda num_1, num_2: num_1 * num_2
for i1 in range(1,10):
    for i2 in range(1,10):
        print(str(i1) + "x" + str(i2) + "=" + str(func(i1, i2)))