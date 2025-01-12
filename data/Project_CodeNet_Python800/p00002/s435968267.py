import sys

def solve():
    for line in sys.stdin:
        a, b = map(int, line.split())

        c = a + b

        if c == 0:
            print(1)
        else:
            ans = 0

            while c > 0:
                ans += 1
                c //= 10

            print(ans)

if __name__ == '__main__':
    solve()