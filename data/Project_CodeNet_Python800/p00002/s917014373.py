while True:
    try:
        input_line = input()
        if input_line == '':
            break
        else:
            print(len(str(sum(map(int, input_line.split())))))
    except EOFError:
        break
