x = 1
y = 1
while x < 10:
    while y < 10:
        print('{}x{}={}'.format(x, y, x*y))
        y += 1
    x += 1
    y = 1