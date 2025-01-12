# usr/bin/python
# coding: utf-8
################################################################################
#Write a program which prints multiplication tables in the following format:
#
#1x1=1
#1x2=2
#.
#.
#9x8=72
#9x9=81
#
################################################################################

if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            print("{0}x{1}={2}".format(i,j,i*j))
    exit(0)