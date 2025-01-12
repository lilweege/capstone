import sys

if __name__ == '__main__':
    for line in sys.stdin:
        (x,y) = map(int,line.split())
        print(len(str(x+y)))