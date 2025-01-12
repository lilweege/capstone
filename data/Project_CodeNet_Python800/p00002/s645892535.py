import sys,math
for i in sys.stdin.readlines():
    if not i.strip():break
    a, b = map(int, i.split())
    print int(math.log10(a+b))+1