def get_input():
    while True:
        try:
            yield ''.join(raw_input())
        except EOFError:
            break

if __name__ == '__main__':
    l = map(int, list(get_input()))
    for elem in sorted(l)[:-4:-1]:
        print elem