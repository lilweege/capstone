kuku= [1, 2, 3, 4, 5, 6, 7, 8, 9]

for a in kuku:
    for b in kuku:
        print(a, end='')
        print("x", end='')
        print(b, end='')
        print("=", end='')
        print( a*b )
