import itertools

l = [int(input()) for i in range(10)]
r = reversed(sorted(l))
for x in itertools.islice(r, 3):
    print(x)