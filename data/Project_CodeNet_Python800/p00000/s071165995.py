a = [i for i in range(1,10)]
for b in a:
    for c in a:
        print('{}x{}={}'.format(b,c,b*c))
