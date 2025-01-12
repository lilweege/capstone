# usr/bin/python
# coding: utf-8
################################################################################
# Digit Number
# Write a program which computes the digit number of sum of two integers a and b.
#
# Input
# There are several test cases. Each test case consists of two non-negative integers a and b which are separeted by a space in a line. The input terminates with EOF.
#
# Constraints
# 0 ??? a, b ??? 1,000,000
# The number of datasets ??? 200
# Output
# Print the number of digits of a + b for each data set.
#
# Sample Input
# 5 7
# 1 99
# 1000 999
# Output for the Sample Input
# 2
# 3
# 4
#
################################################################################

import math
import fileinput

if __name__ == "__main__":
    for line in fileinput.input():
        a = int(line.split(" ")[0])
        b = int(line.split(" ")[1])
        data_size = int(math.log10(a+b) + 1)
        print(data_size)
    exit(0)
  