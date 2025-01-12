def main():
    def inputs():
        li = []
        count = 0
        try:
            while count < 200:
                li.append(input())
                count += 1
        except EOFError:
            return li
        return li

    li = inputs()
    for x in li:
        a = x.split(" ")
        result = len(str(int(a[0]) + int(a[1])))
        print(result)
    return None

if __name__ == '__main__':
    main()