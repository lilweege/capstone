def puts(x, y):
    print '{0}x{1}={2}'.format(x, y, x*y)

[puts(i ,j) 
    for i in range(1, 10)
    for j in range(1, 10)]