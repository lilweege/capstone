from math import log10, floor
while True:
    try:
        w = input()
    except EOFError:
        break
    w = list(map(int, w.split()))
    print(floor(log10(sum(w))+1))