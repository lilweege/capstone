def main():
    """ ????????? """
    m = []
    for i in range(10):
        m.append(int(input()))
    m.sort(reverse=True)
    for i in range(3):
        print(m[i])

if __name__ == '__main__':
    main()