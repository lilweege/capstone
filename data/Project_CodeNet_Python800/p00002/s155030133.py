import sys
def main():
    for line in sys.stdin:
        A = list(map(int,line.split()))
        C = A[0]+A[1]
        count = 0
        while True:
            C/=10
            if C < 1:
                break
            count += 1
        print(count+1)

if __name__ == '__main__':
    main()