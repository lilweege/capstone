while True:
    try:
        line = input()
    except EOFError:
        break
    s = sum(map(int, line.split()))
    num = 0
    for c in str(s):
        if c.isdigit():
            num += 1
    print(num)