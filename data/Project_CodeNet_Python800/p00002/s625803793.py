while True:
    try:
        a, b = (int(x) for x in raw_input().split())
        s = a + b
        num_digits = 0
        while s > 0:
            s /= 10
            num_digits += 1
        print num_digits
    except EOFError:
        break

