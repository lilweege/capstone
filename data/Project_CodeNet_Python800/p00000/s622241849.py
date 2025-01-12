def main():
    for i in range(9):
        multiplicand = i+1
        for i in range(9):
            multiplier = i+1
            answer = multiplicand * multiplier
            print(str(multiplicand) + 'x' + str(multiplier) + '=' + str(answer))

if __name__ == '__main__':
    main()