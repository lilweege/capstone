import sys, math

def run():
    N = []
    for n in sys.stdin:
        a,b = map(int, n.split())
        N.append((a,b))

    for a,b in N:
        print(math.floor(math.log10(a+b)) + 1)

if __name__ == '__main__':
    run()


