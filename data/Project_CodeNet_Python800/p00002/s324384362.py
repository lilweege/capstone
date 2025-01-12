import fileinput
for line in fileinput.input():
    a, b = map(int, line.split())
    print(len(str(a + b)))