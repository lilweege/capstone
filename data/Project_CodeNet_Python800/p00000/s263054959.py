import sys
write=sys.stdout.write

for i in range(1,10):
    for j in range(1,10):
        write(str(i))
        write('x')
        write(str(j))
        write('=')
        write(str(i*j))
        print()