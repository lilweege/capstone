def compute_digits_num(a,b):
    c = a + b
    s = 0
    for c in str(c):
        s += 1
    return s

try:
    while True:
        a, b = list(map(int, input().split()))
        print(compute_digits_num(a,b))
except:
    pass
