# -*-coding:utf-8

import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        digit = 0
        tokens = list(map(int, line.strip().split()))
        a, b = tokens[0], tokens[1]
        num = a + b

        print(len(str(num)))