for i in range(1, 10):
    for j in range(1, 10):
        fmt = format("{0}x{1}={2}")
        g = fmt.format(i, j, i*j)
        print(g)