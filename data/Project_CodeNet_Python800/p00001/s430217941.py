def main():
    N=10
    l = list()
    for i in range(N):
        l.append(int(input()))
    l.sort(reverse=True)
    for x in l[:3]:
        print(x)

if __name__=='__main__':
    main()