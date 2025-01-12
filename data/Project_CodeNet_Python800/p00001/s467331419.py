def main():
    l = []
    for _ in range(10):
        l.append(int(input()))
    l = sorted(l, reverse=True)
    for i in range(3):
        print(l[i])
    return None

if __name__ == '__main__':
    main()