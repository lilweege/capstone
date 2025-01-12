import fileinput as fi
if __name__ == "__main__":
    for i in fi.input():
        a,b = list(map(int,i.strip().split()))
        print(len(str(a+b)))