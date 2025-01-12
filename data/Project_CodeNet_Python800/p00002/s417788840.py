import sys
def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(len(str(a + b)))

if __name__ == "__main__":
    main()