import sys
if __name__ == "__main__":
    for i in sys.stdin:
        a,b = list(map(int,i.strip().split()))
        print(len(str(a+b)))