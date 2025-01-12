# coding: utf-8

def getint():
    return int(input().rstrip())

def main():
    ls = []
    num_of_mount = 10
    num_of_top = 3
    
    for i in range(num_of_mount):
        ls.append(getint())

    ls.sort(reverse=True)

    for i in range(num_of_top):
        print(ls[i])

if __name__ == '__main__':
    main()