# -*-coding:utf-8

lineNum = int(input())

for i in range(lineNum):
    line = input()
    tokens = list(map(int, line.strip().split()))

    tokens.sort()

    a, b, c = tokens[0], tokens[1], tokens[2]

    if pow(a,2)+pow(b,2) == pow(c,2):
        print('YES')
    else:
        print('NO')