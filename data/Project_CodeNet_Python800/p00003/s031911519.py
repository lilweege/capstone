def main():
    n = int(input())
    for i in range(n):
        Array = list(map(int,input().split()))
        Array.sort()
        if Array[2]**2 == Array[0]**2 + Array[1]**2:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()