# coding: utf-8
#Problem Name: Digit Number
#ID: tabris
#Mail: t123037@kaiyodai.ac.jp

while True:
    try:
        a,b = map(int,raw_input().split(' '))
        print len(str(a+b))
    except:
        break

'''
Sample Input
5 7
1 99
1000 999
'''