import sys
strs = sys.stdin.readlines()
for s in strs:
    a, b = map(int, s.split())
    print(len(str(a + b)))