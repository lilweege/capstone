if __name__ == "__main__":
    a = []
    for i in range(0,10):
        val = input()
        a.append(int(val))

    a.sort()
    a.reverse()
    for i in range(0,3):
        print(a[i])