a = [x + 1 for x in range(9)]
for i in a:
    for j in a:
        print('{}x{}={}'.format(i, j, i * j))