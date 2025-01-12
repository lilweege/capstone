import sys


def main():
    l = []
    for line in sys.stdin.readlines():
        l.append(int(line.rstrip()))

    for _ in range(3):
        print max(l)
        l.remove(max(l))

main()