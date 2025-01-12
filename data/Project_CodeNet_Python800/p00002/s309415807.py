from __future__ import absolute_import, print_function, unicode_literals
import sys

for line in sys.stdin:
    print(len(str(sum(int(n) for n in line.split()))))