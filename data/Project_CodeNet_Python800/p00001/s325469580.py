import sys
def solve():

    a = []
    for line in sys.stdin:
        a.append(int(line))

    a.sort()
    a.reverse()
    for k in xrange(3):
        print a[k]
if __name__ == '__main__':
    solve()