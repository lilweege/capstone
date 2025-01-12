def main():
    while True:
        try:
            a, b = (int(x) for x in input().split())
            print(len(str(a+b)))
        except EOFError:
            break
main()
