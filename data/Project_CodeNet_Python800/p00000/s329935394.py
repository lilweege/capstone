s=0
t=0
for i in range(9):
    s+=1
    for j in range(9):
        if t==9:
            t=1
        else:
            t+=1
        print(f'{s}x{t}={s*t}')
