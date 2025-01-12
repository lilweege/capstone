import sys


def main():
    for line in sys.stdin.readlines():
        a,b = [int(n) for n in line.split()]
        ret = a + b
        print len(str(ret))


main()