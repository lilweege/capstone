for x in range(9):
    x = x + 1
    for y in range(9):
        y = y + 1
        print(x.__str__() + 'x' + y.__str__() + '=' + (x * y).__str__() )