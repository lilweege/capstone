# coding: utf-8
# Your code here!

for line in open(0).readlines():
    a, b = map(int, line.split())
    c = a+b
    ans = +(c == 0)
    while c:
        ans += 1
        c //= 10
    print(ans)
