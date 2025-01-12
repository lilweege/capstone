import sys
for e in sys.stdin.readlines():
 print(len(str(eval('+'.join(e.split())))))
