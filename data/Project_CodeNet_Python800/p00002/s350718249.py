import math

def main():
    data = []
    while 1:
        try:
            n = input().split()
            a = int(n[0])
            b = int(n[1])
            ans = int(math.log10(a+b)+1)
            data.append(ans)
        except EOFError:
            break

    for i in data:
        print(i)

if __name__ == "__main__":
    main()