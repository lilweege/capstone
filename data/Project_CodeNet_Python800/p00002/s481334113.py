from sys import stdin

for s in stdin:
    s = s[:-1]
    i = s.index(' ')
    a = int(s[0:i])
    s = s[i+1:]
    b = int(s)
    print len(str(a+b))