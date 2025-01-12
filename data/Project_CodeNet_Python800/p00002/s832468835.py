import math

def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

line = list(get_input())
for l in range(len(line)):
    a,b = [int(i) for i in line[l].split()]
    S = a + b
    keta = 0
    while S > 0:
        S = math.floor(S / 10)
        keta = keta + 1
    print(keta)


