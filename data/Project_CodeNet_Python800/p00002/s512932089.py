import fileinput

if __name__ == "__main__":
    for line in fileinput.input():
        v = line.split(" ")
        print(len(str(sum([int(i) for i in v]))))