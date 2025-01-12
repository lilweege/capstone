import sys
 
[print(len(str(y[0] + y[1]))) for y in [[int(z) for z in x.split()] for x in sys.stdin]]