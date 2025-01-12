import sys


def solve():
    a = []
    for line in sys.stdin:
        digit_list = line.split(' ')
        new_list = []
        for s in digit_list:
            new_list.append(int(s))
        a.append((new_list))
    for j in a:

        print str(len(str(sum(j))))	

if __name__ == '__main__':
    solve()