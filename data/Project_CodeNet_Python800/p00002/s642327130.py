import sys

def solve():
    while True:
        try:
            a, b = map(int, sys.stdin.readline().split())
            c = a + b

            if c == 0:
                print(1)
            else:
                ans = 0

                while c > 0:
                    ans += 1
                    c //= 10

                print(ans)

        except:
            return

if __name__ == '__main__':
    solve()