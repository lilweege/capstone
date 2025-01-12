#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sato
#
# Created:     19/10/2013
# Copyright:   (c) sato 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def kuku():
    for x in range(1,10):
        for y in range(1,10):
            print (str(x) + 'x' +  str(y) + '=' + str(x*y))

if __name__ == '__main__':
    kuku()