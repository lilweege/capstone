import sys

def main():
    for line in sys.stdin:
        arr = map(int,line.split())
        print len(str(arr[0]+arr[1]))

if __name__ == '__main__':
    main()