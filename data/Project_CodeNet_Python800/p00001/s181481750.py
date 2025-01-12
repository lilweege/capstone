def main():
    a = []
    for i in range(10):
        a.append(int(input()))

    a.sort()
    a.reverse()

    for i in range(3):
        print(a[i])

if __name__ == '__main__':
    main()