from __future__ import absolute_import, print_function, unicode_literals

for a in xrange(1, 10):
    for b in xrange(1, 10):
        print('{}x{}={}'.format(a, b, a * b))