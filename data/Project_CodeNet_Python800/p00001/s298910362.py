# coding: utf-8
"""
aizu 0001
"""

import sys

# @profile
def main():
    mountaines=[]
    for line in sys.stdin:
        mountaines.append(int( line ))
    mountaines.sort(reverse=True)
    for index,x in enumerate( mountaines ):
        print x
        if index >=2:
            break
if __name__ == '__main__':
    main()