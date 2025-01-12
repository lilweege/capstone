
n = [0,0,0,0,0,0,0,0,0,0]

for i in range( 0, 10 ):
    n[i] = int(input())

mv = 0
ma = 0

for i in range( 0, 3 ):
    for j in range( 0, 10 ):
        if mv < n[j]:
            mv = n[j]
            ma = j
    print( mv )
    n[ma] = -1
    mv = 0