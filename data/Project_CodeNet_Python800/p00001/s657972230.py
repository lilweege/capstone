# -*- coding: utf-8 -*-

hills_list = []
while len(hills_list) != 10:
    hills = raw_input()
    if (10000 >= int(hills)) and (int(hills) >= 0):
        hills_list.append(int(hills))
hills_list.sort()
print hills_list[-1]
print hills_list[-2]
print hills_list[-3]