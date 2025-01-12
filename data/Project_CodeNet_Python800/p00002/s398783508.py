#!/usr/bin/env python

dn = lambda a, b: len(str(a+b))
get = lambda: [int(x) for x in raw_input().split()]

if __name__ == "__main__":
    while True:
        try:
            print "%d" % dn(*get())
        except:
            break