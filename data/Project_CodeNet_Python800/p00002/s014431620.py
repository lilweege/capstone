# -*- coding: utf-8 -*-

"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002
"""

while True:
    try:
        a = raw_input().split()
        #print a
        c = 0
        for b in a:
            c = c + int(b)
        print len(str(c))
    except EOFError:
        break