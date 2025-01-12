#coding:utf-8

import sys

if __name__ == '__main__':

    nums = []

    for line in sys.stdin:
        if line == "\n":
            break
        else :
            nums.append(int(line))

    for n in sorted(nums, reverse=True)[:3]:
        print(n)