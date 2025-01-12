import fileinput

if __name__ == '__main__':
    for line in fileinput.input():
        tokens = line.strip().split()
        a, b = int(tokens[0]), int(tokens[1])
        c = a+b
        print(len(str(c)))