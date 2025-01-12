
#!/usr/bin/env python
# coding: utf-8


def main():
    while 1:
        try:
            input_data = raw_input()
        except EOFError:
            break
        print sum(map(int, input_data.split(" "))).__str__().__len__()

if __name__ == '__main__':
    main()