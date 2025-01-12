import sys

def main():
    """ ????????? """
    istr = sys.stdin.read()
    wi = istr.splitlines()
    for i in wi:
        a = list(map(int,i.split()))
        b = str(a[0] + a[1])
        print(len(b))

if __name__ == '__main__':
    main()