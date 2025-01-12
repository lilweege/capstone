import sys
for e in sys.stdin:
 print(len(str(eval('+'.join(e.split())))))
