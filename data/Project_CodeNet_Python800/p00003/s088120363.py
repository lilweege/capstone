from __future__ import absolute_import, print_function, unicode_literals
import sys

def judge(a, b, c):
    print('YES' if (a == b + c or b == c + a or c == a + b) else 'NO')

sys.stdin.readline()
for line in sys.stdin:
    judge(*(int(n) ** 2 for n in line.split()))