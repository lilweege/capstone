# -*- coding: utf-8 -*-

def qq(limit=9):
    qq_str = ''
    for i in range(1, limit+1):
        for j in range(1, limit+1):
            qq_str += str(i) + 'x' + str(j) + '=' + str(i*j)
            if i != limit or j != limit:
                qq_str += '\n'
    return qq_str

def main():
    print(qq())

if __name__ == '__main__':
    main()