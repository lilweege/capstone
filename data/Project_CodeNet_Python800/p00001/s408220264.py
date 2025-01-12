import fileinput

def main():
    numbers = []
    for line in fileinput.input():
        numbers.append(int(line))
    numbers = sorted(numbers, reverse=True)
    for n in numbers[0:3]:
        print n

main()