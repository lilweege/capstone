def main():
    N = int(input())
    a = []
    for _ in range(N):
        a.append(list(map(int, input().split())))

    for x in range(N):
        a[x].sort(reverse = True)
        if a[x][0] ** 2 == a[x][1] ** 2 + a[x][2] ** 2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()