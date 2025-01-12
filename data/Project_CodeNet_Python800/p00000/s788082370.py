import sys

def solve():
    for i in range(1, 10):
        for j in range(1, 10):
            print('{}x{}={}'.format(i, j, i*j))

if __name__ == '__main__':
    solve()