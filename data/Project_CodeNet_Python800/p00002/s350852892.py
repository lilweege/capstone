def digits(n):
    if n < 10: return 1
    c = 0
    while n > 0:
        c += 1
        n = n // 10

    return c

while 1:
    try:
        inp = input()
    except EOFError:
        break
    else:
        n, m = inp.split(' ')
        n = int(n)
        m = int(m)
        print(digits(n + m))